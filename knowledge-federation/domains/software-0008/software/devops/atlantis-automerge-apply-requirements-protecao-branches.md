---
id: software.devops.tranche10.000946
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
fontes: ["https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md", "https://www.runatlantis.io/docs/using-atlantis.html", "https://www.runatlantis.io/docs/how-atlantis-works.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Atlantis: Automerging de Pull Requests, método de merge (--auto-merge-method) e requisito undiverged

## Em uma frase
O recurso de **Automerging** do Atlantis faz o merge automático do Pull Request assim que todos os planos do PR tiverem sido aplicados com sucesso via `atlantis apply`, permitindo controlar o método de merge (`--auto-merge-method`) ou desabilitá-lo pontualmente (`--auto-merge-disabled`).

## Por que importa
Como o Atlantis aplica as mudanças de infraestrutura antes do merge do PR, se o engenheiro rodar `atlantis apply`, ver que deu certo e esquecer de clicar no botão "Merge Pull Request" no GitHub/GitLab, a branch `main` ficará desatualizada em relação à nuvem e o diretório continuará bloqueado (`Locked`) impedindo o restante da equipe de trabalhar.

## Como funciona
Quando `automerge: true` está habilitado (no `atlantis.yaml` ou via flag `--automerge` no servidor), ao executar `atlantis apply` o Atlantis verifica se todos os planos gerados naquele Pull Request já foram aplicados com sucesso; caso positivo, o Atlantis realiza o merge automático do PR via API do GitHub/GitLab/Bitbucket e libera todos os locks. Conforme documenta `Using Atlantis`, no momento do comentário `atlantis apply`, o usuário pode passar **`--auto-merge-disabled`** para impedir o automerge naquele comando específico ou **`--auto-merge-method <method>`** (ex.: `squash`, `merge`, `rebase` no GitHub) para escolher o método de merge.

## Exemplo
```text
# Aplicar todos os planos pendentes do PR especificando o método squash para o automerge ou desabilitando o automerge
atlantis apply --auto-merge-method squash
atlantis apply -p network-staging --auto-merge-disabled
```

## Limites e trade-offs
Se um Pull Request modifica 3 projetos diferentes (`proj-a`, `proj-b` e `proj-c`) e você executa apenas `atlantis apply -p proj-a`, o Automerging **não** fará o merge do PR ainda porque `proj-b` e `proj-c` continuam com planos pendentes não aplicados; o automerge só dispara quando 100% dos planos do PR foram aplicados (ou quando `atlantis apply` sem filtros aplica todos de uma vez).

## Como verificar
Configure `automerge: true` em um repositório de homologação, aprove o PR, comente `atlantis apply` e confirme que o PR é mergeado automaticamente e que o lock desaparece da UI do Atlantis.

## Conexões
- [[atlantis-workflows-customizados-repos-yaml-server-side]] — Veja também: Atlantis: configuração server-side (repos.yaml), restrição de allowed_overrides e Custom Workflows ($PLANFILE).
- [[atlantis-operacoes-import-state-rm-destroy-pr]] — Veja também: Atlantis: importação de recursos (atlantis import), remoção de estado (state rm) e planos destrutivos (-destroy) via PR.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-comandos-pull-request-plan-apply-flags-workspaces]] — Referência cruzada direta com atlantis-comandos-pull-request-plan-apply-flags-workspaces.
- [[atlantis-bloqueio-diretorio-workspace-locking-unlock]] — Referência cruzada direta com atlantis-bloqueio-diretorio-workspace-locking-unlock.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/how-atlantis-works.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
