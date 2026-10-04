---
id: software.devops.tranche12.001138
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/direnv/direnv/master/README.md", "https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md", "https://github.com/direnv/direnv"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# direnv: Isolamento de Contexto Multi-Cluster e Multi-Cloud (KUBECONFIG, AWS_PROFILE e TF_WORKSPACE)

## Em uma frase
Em operações DevOps e SRE, o `direnv` previne acidentes graves de execução no cluster ou conta cloud errada ao vincular `KUBECONFIG`, `AWS_PROFILE`, `CLOUDSDK_ACTIVE_CONFIG_NAME` e variáveis `TF_VAR_*` ao diretório de cada ambiente (`envs/staging`, `envs/prod`).

## Por que importa
Quando todos os terminais compartilham o mesmo arquivo global `~/.kube/config`, mudar o contexto com `kubectl config use-context prod` em uma aba do terminal muda instantaneamente o contexto de todas as outras abas abertas, causando comandos destrutivos no cluster errado.

## Como funciona
Ao estruturar repositórios de infraestrutura por diretório de ambiente e definir em cada `.envrc` um `export KUBECONFIG="$PWD/kubeconfig.yaml"` e `export AWS_PROFILE="org-prod"`, cada aba do terminal fica estritamente isolada ao ambiente da pasta em que se encontra, sem interferir em outros terminais.

## Exemplo
```bash
# Em infra/live/production/.envrc:
export AWS_PROFILE="acme-production"
export AWS_DEFAULT_REGION="sa-east-1"
export KUBECONFIG="$PWD/.kube/prod-cluster.yaml"
export TF_IN_AUTOMATION="false"
env_vars_required AWS_PROFILE KUBECONFIG
```

## Limites e trade-offs
Armazenar credenciais estáticas de longa duração (`AWS_SECRET_ACCESS_KEY` ou tokens de admin) em texto puro dentro de um `.envrc` commitado no Git compromete a segurança da conta cloud.

## Como verificar
Commit apenas nomes de perfis (`AWS_PROFILE`), regiões e caminhos relativos no `.envrc` compartilhado, ou mantenha segredos locais em um `.env.local` ignorado pelo Git e carregado via `dotenv_if_exists .env.local`.

## Conexões
- [[direnv-extensoes-customizadas-direnvrc-config-lib]] — Veja também: direnv: Extensões Pessoais e Corporativas em ~/.config/direnv/direnvrc e lib/*.sh.
- [[direnv-toml-configuracao-global-load-dotenv-strict-env]] — Veja também: direnv: Configuração Global no direnv.toml (load_dotenv, strict_env e warn_timeout).

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
