---
id: software.devops.tranche10.000950
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

# Atlantis: execução paralela de planos (parallel_plan), customização do executável (--executable-name) e modo --verbose

## Em uma frase
Em monorepos com dezenas de projetos Terraform, o Atlantis acelera o feedback habilitando **`parallel_plan: true`** no `atlantis.yaml`, permite customizar o nome do comando invocado nos comentários (`--executable-name`, `run` ou `@GithubUser`) e anexar logs detalhados de diagnóstico com **`--verbose`**.

## Por que importa
Quando um Pull Request altera um módulo base consumido por 15 projetos diferentes no mesmo repositório, rodar 15 `terraform plan` de forma estritamente sequencial um após o outro pode levar 20 minutos; além disso, empresas que rodam múltiplas instâncias do Atlantis (ex.: uma instância para AWS e outra para GCP no mesmo repositório) precisam que cada instância responda a um nome de comando diferente no comentário do PR.

## Como funciona
(1) **Paralelismo (`parallel_plan` e `parallel_apply`)**: habilitar `parallel_plan: true` no `atlantis.yaml` faz o Atlantis executar os planos de projetos independentes em goroutines paralelas (controladas por `--parallel-pool-size`, padrão 15); (2) **Customização do nome do comando**: conforme a dica na seção inicial de `Using Atlantis` (`runatlantis.io/docs/using-atlantis.html`), além do padrão `atlantis help` (configurável via `--executable-name`, ex.: `atlantis-aws plan`), o Atlantis também aceita o nome global `run help` ou menção direta ao usuário do bot `@GithubUser help`; e (3) **Diagnóstico (`--verbose`)**: adicionar `--verbose` ao final de qualquer comando (`atlantis plan --verbose` ou `atlantis apply --verbose`) anexa o log interno do Atlantis ao comentário do PR.

## Exemplo
```text
# Executar um plano anexando os logs internos detalhados do servidor Atlantis (--verbose) ao comentário do PR
atlantis plan -p network-staging --verbose
```

## Limites e trade-offs
Embora `parallel_plan: true` seja seguro e altamente recomendado para acelerar PRs com múltiplos projetos, tenha cautela ao habilitar `parallel_apply: true` caso haja dependências implícitas entre diretórios diferentes no seu repositório (por exemplo, o diretório `eks-cluster` precisa terminar de ser aplicado antes que o diretório `k8s-addons` tente conectar no cluster); para projetos com ordem de dependência, mantenha `parallel_apply: false` ou configure `execution_order_group`.

## Como verificar
Habilite `parallel_plan: true` no `atlantis.yaml` de um repositório multi-projeto e observe o tempo total reduzido ao rodar `atlantis plan` sobre múltiplos projetos simultaneamente.

## Conexões
- [[atlantis-seguranca-webhooks-segredos-autenticacao-implantacao]] — Veja também: Atlantis: modelo de segurança do servidor, proteção contra PRs maliciosos, Drift Detection API e implantação em Kubernetes.
- [[atlantis-automacao-terraform-pull-requests-webhooks]] — Referência cruzada direta com atlantis-automacao-terraform-pull-requests-webhooks.
- [[atlantis-comandos-pull-request-plan-apply-flags-workspaces]] — Referência cruzada direta com atlantis-comandos-pull-request-plan-apply-flags-workspaces.
- [[atlantis-configuracao-repositorio-atlantis-yaml-autoplan-when-modified]] — Referência cruzada direta com atlantis-configuracao-repositorio-atlantis-yaml-autoplan-when-modified.

## Fontes
- [Atlantis Official Documentation — Using Atlantis (PR Commands plan/apply, -d/-p/-w Flags, env/{workspace}.tfvars & Automerge Flags)](https://raw.githubusercontent.com/runatlantis/atlantis/main/README.md) — Guia oficial de uso do Atlantis detalhando comandos via comentários de PR, inclusão automática de env/{workspace}.tfvars, passagem de flags após -- e opções de automerge; consultado em 2026-10-03.
- [Atlantis Official Documentation — Locking & How Atlantis Works (Directory/Workspace Locks, Global Apply Lock, atlantis unlock & Drift Detection)](https://www.runatlantis.io/docs/using-atlantis.html) — Documentação oficial de bloqueio (Locking) do Atlantis explicando o lock por diretório e workspace até o merge do PR, Global Apply Lock fail-closed, atlantis unlock, relação com Terraform State Locking e Drift Detection; consultado em 2026-10-03.
- [RunAtlantis — Official GitHub README.md](https://www.runatlantis.io/docs/how-atlantis-works.html) — README oficial do repositório runatlantis/atlantis; consultado em 2026-10-03.
