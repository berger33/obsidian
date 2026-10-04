---
id: software.devops.tranche11.001098
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

# Reprodutibilidade entre máquinas e CI no mise: versões flutuantes de série versus pinos exatos e mise.lock

## Em uma frase
Enquanto pedidos de versão por prefixo (como `node = "24"` ou `python = "3.14"`) selecionam a release mais recente daquela série no momento da instalação, o `mise` suporta **pinos exatos de versão** e arquivos de trava (**`mise.lock`**) para garantir que todos os desenvolvedores e pipelines de CI utilizem exatamente o mesmo binário resolvido.

## Por que importa
Se o arquivo `mise.toml` declarar apenas `terraform = "1"` ou `node = "24"`, um desenvolvedor que rodou `mise install` no mês passado pode estar na `24.1.0` enquanto o runner de CI hoje baixa a `24.2.0`, introduzindo diferenças sutis de comportamento ou quebras inesperadas no pipeline.

## Como funciona
Conforme destacam o README oficial (`jdx/mise`) e a seção *Run a task* do guia *Getting started* (`mise.jdx.dev/getting-started.html`), quando você executa `mise use node@24`, o `mise` grava `node = "24"` no `mise.toml`, o que representa uma solicitação para qualquer release dentro da série 24 do Node.js (*it is not an exact pin*). Para garantir reprodutibilidade estrita entre todas as estações da equipe e os agentes de integração contínua, a documentação orienta duas práticas: especificar a versão completa exata (ex.: `mise use node@24.0.1`) ou utilizar o suporte a **lockfiles (`mise.lock`)** para compartilhar as versões exatas resolvidas e seus respectivos checksums no repositório Git.

## Exemplo
```bash
# Fixar uma versão exata no mise.toml e inspecionar as versões exatas atualmente resolvidas no projeto
mise use node@24.0.0
mise ls --current
```

## Limites e trade-offs
Fixar versões exatas ou usar lockfile impede que novas versões patch de segurança sejam instaladas silenciosamente em cada novo `mise install`; por isso, combine o pin exato / lockfile com atualizações periódicas revisadas em Pull Request (`mise upgrade`).

## Como verificar
Execute `mise ls --current` na sua máquina local e no job de CI, confirmando que a coluna de versão instalada coincide até o número de patch.

## Conexões
- [[mise-diagnostico-doctor-rate-limit-github-token-ci]] — Veja também: Diagnóstico com mise doctor, mitigação de GitHub API Rate Limiting e uso em CI/CD.
- [[mise-gerenciamento-ambientes-diretivas-env-dotenv-hierarquia]] — Veja também: Gerenciamento de variáveis de ambiente no mise: seção [env], carregamento de arquivos .env e hierarquia de configuração.
- [[mise-configuracao-projeto-mise-toml-tools-env-tasks]] — Referência cruzada direta com mise-configuracao-projeto-mise-toml-tools-env-tasks.
- [[mise-comandos-operacionais-use-install-exec-run-global]] — Referência cruzada direta com mise-comandos-operacionais-use-install-exec-run-global.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://mise.jdx.dev/getting-started.html) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
