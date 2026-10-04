---
id: software.devops.tranche10.000943
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md", "https://www.runatlantis.io/docs/locking.html", "https://www.runatlantis.io/docs/using-atlantis.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atlantis: sistema de Locking por diretório e workspace, Global Apply Lock e relação com o Terraform State Lock

## Em uma frase
Conforme detalha a página oficial `Locking` (`runatlantis.io/docs/locking.html`), quando um `plan` é executado em um PR, o Atlantis **bloqueia (Locks)** aquele diretório e workspace até que o PR seja mergeado/fechado ou que o plano seja descartado manualmente (`atlantis unlock`), operando em uma camada acima do Terraform State Locking.

## Por que importa
Como o `atlantis apply` roda na branch do Pull Request **antes** do merge na `main`, se um segundo desenvolvedor abrisse outro PR alterando o mesmo diretório/workspace antes do primeiro PR ser mergeado, o segundo PR geraria um plano inválido ou reverteria as mudanças recém-aplicadas pelo primeiro PR. O bloqueio em nível de PR do Atlantis impede essa condição de corrida.

## Como funciona
(1) **Escopo do Lock**: apenas o par **(diretório do repositório + workspace do Terraform)** fica bloqueado para aquele Pull Request — outros diretórios ou outros workspaces no mesmo repositório continuam livres para outros PRs planejarem e aplicarem normalmente; (2) se outro PR tentar rodar `plan` no diretório/workspace bloqueado, o Atlantis posta um erro com link direto para o PR que detém o lock; (3) **Global Apply Lock (fail-closed)**: antes de rodar `atlantis apply`, o Atlantis também verifica o bloqueio global de apply; se não conseguir alcançar o backend de lock, ele **falha fechado (`fails closed`)** e rejeita o apply; e (4) **Unlocking**: o lock é liberado automaticamente quando o PR é mergeado ou fechado, ou manualmente comentando **`atlantis unlock`** no PR (ou clicando em *Discard Plan and Unlock* na interface web do Atlantis).

## Exemplo
```text
# Liberar manualmente os planos e os locks de diretório/workspace mantidos pelo Pull Request atual sem fazer merge
atlantis unlock
```

## Limites e trade-offs
Conforme explica a seção `Relationship to Terraform State Locking` da documentação oficial, o lock do Atlantis **não substitui nem conflita** com o **Terraform State Locking** (como o lock no S3/DynamoDB ou GCS): o lock nativo do Terraform dura apenas os segundos/minutos em que o comando `terraform apply` está rodando para evitar escrita concorrente no arquivo `.tfstate`, enquanto o lock do Atlantis dura todo o ciclo de vida do Pull Request (horas ou dias) para impedir que dois PRs trabalhem sobre o mesmo estado ao mesmo tempo.

## Como verificar
Acesse a URL da interface web do servidor Atlantis para visualizar todos os locks ativos no painel `Locks` ou comente `atlantis unlock` em um PR para descartar o plano e liberar o diretório/workspace.

## Conexões
- [[atlantis-comandos-pull-request-plan-apply-flags-workspaces]] — Veja também: Atlantis: comandos de comentário em PR (atlantis plan e apply), seleção de projeto (-d, -p, -w) e arquivos env/{workspace}.tfvars.
- [[atlantis-configuracao-repositorio-atlantis-yaml-autoplan-when-modified]] — Veja também: Atlantis: configuração de projetos no repositório com atlantis.yaml (projects, workspace, autoplan e when_modified).
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-automerge-apply-requirements-protecao-branches]] — Referência cruzada direta com atlantis-automerge-apply-requirements-protecao-branches.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/locking.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/using-atlantis.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
