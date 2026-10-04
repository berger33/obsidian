---
id: software.devops.tranche11.001099
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://mise.jdx.dev/getting-started.html", "https://raw.githubusercontent.com/jdx/mise/main/README.md", "https://github.com/jdx/mise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Gerenciamento de variáveis de ambiente no mise: seção [env], carregamento de arquivos .env e hierarquia de configuração

## Em uma frase
A seção **`[env]`** do `mise.toml` permite declarar variáveis de ambiente específicas por projeto e carregar arquivos `.env` automaticamente, aplicando sobreposição hierárquica desde a configuração global (`~/.config/mise/config.toml`) até os diretórios de projetos e ambientes locais.

## Por que importa
Em vez de manter scripts `source env.sh` manuais ou exigir a instalação separada do `direnv` com arquivos `.envrc` adicionais, o `mise` gerencia tanto os binários quanto as variáveis de ambiente (`KUBECONFIG`, `AWS_PROFILE`, `NODE_ENV`, `DATABASE_URL`) no mesmo ciclo de ativação de diretório e execução de tarefas.

## Como funciona
Conforme documentado em `mise.jdx.dev/getting-started.html` (*Set an environment variable* e *Project configuration or global defaults?*): (1) chaves definidas sob `[env]` no `mise.toml` são injetadas automaticamente quando você executa `mise exec -- <cmd>`, `mise run <task>` ou quando entra no diretório com `mise activate` ativo no shell; (2) é possível usar diretivas de ambiente para carregar variáveis a partir de arquivos `.env` locais (que permanecem no `.gitignore` para não vazar segredos no Git, enquanto variáveis não sensíveis ficam versionadas no `mise.toml`); e (3) `mise config ls` exibe todos os arquivos de configuração ativos na hierarquia e a ordem em que são aplicados.

## Exemplo
```toml
# Configurar variáveis de ambiente de desenvolvimento e apontar um KUBECONFIG isolado por projeto no mise.toml
[tools]
kubectl = "1.31"
helm = "3.16"

[env]
KUBECONFIG = "./.kube/config-dev.yaml"
HELM_NAMESPACE = "desenvolvimento"
```

## Limites e trade-offs
Nunca versione segredos reais (chaves privadas, tokens de produção ou senhas de banco) diretamente na seção `[env]` do `mise.toml` commitado no Git; mantenha apenas valores padrão de desenvolvimento no `mise.toml` e carregue credenciais sensíveis de arquivos `.env` ignorados pelo Git ou de gerenciadores de segredos como **SOPS** ou **HashiCorp Vault**.

## Como verificar
Execute `mise exec -- env | grep -E "KUBECONFIG|HELM_NAMESPACE"` para confirmar que as variáveis declaradas no `mise.toml` foram injetadas corretamente no processo filho.

## Conexões
- [[mise-reprodutibilidade-lockfile-mise-lock-pinos-versao]] — Veja também: Reprodutibilidade entre máquinas e CI no mise: versões flutuantes de série versus pinos exatos e mise.lock.
- [[mise-task-runner-integrado-bootstrap-maquinas-ide]] — Veja também: Task Runner integrado ([tasks]), Bootstrap de máquinas e integração com IDEs no mise.
- [[mise-configuracao-projeto-mise-toml-tools-env-tasks]] — Referência cruzada direta com mise-configuracao-projeto-mise-toml-tools-env-tasks.
- [[sops-arquivos-binarios-exec-env-exec-file-processos]] — Referência cruzada direta com sops-arquivos-binarios-exec-env-exec-file-processos.
- [[mise-ativacao-shell-activate-vs-shims-matriz-shells]] — Referência cruzada direta com mise-ativacao-shell-activate-vs-shims-matriz-shells.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://mise.jdx.dev/getting-started.html) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
