---
id: software.seguranca.tranche10.000964
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md", "https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Talisman em Escala de Engenharia: Instalação via **Global Git Hook Template (`init.templateDir`)**, Framework **`pre-commit`** e **Husky**

## Em uma frase
Como garantir que o Talisman esteja ativo não apenas em um repositório isolado, mas automaticamente em **todos os repositórios que um desenvolvedor clonar (`git clone`) ou inicializar (`git init`) no futuro**, sem sobrescrever hooks já existentes?

## Por que importa
O Talisman oferece dois caminhos padronizados: **(1) Global Hook Template (`install.bash`)**, que instala o binário em `$HOME/.talisman/bin`, configura o diretório de template global do Git (`git config --global init.templateDir`) e varre um diretório raiz (`SEARCH_ROOT`) criando symlinks nos repositórios locais existentes sem sobrescrever hooks prévios; e **(2) Integração com Gerenciadores de Hooks (`pre-commit` e `Husky`)**!

## Como funciona
Conforme especificado no arquivo oficial `.pre-commit-hooks.yaml` do repositório `thoughtworks/talisman`, o projeto fornece dois IDs oficiais prontos para o `.pre-commit-config.yaml`: **`talisman-commit`** (`entry: cmd --githook pre-commit`, estágio `pre-commit`) e **`talisman-push`** (`entry: cmd --githook pre-push`, estágio `pre-push`)!

## Exemplo
```yaml
# .pre-commit-config.yaml — Integrando o Talisman oficial no estagio pre-commit junto com outros hooks da equipe
repos:
  - repo: https://github.com/thoughtworks/talisman
    rev: v1.36.0
    hooks:
      - id: talisman-commit
```

## Limites e trade-offs
Por que usar o framework `.pre-commit-config.yaml` (ou Husky em projetos Node.js com `talisman --githook pre-commit`) é a abordagem preferida em equipes poliglotas? Porque o Git nativo permite apenas um único arquivo `.git/hooks/pre-commit`, enquanto o `pre-commit` permite encadear **Talisman + Gitleaks + KICS + linters de código** no mesmo commit!

## Como verificar
Para ambientes sem internet na máquina do desenvolvedor, pré-instale o binário `talisman` em `/usr/local/bin` via imagem base ou gerenciador de pacotes interno.

## Conexões
- [[talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity]] — Veja também: Talisman `.talismanrc`: Escopos de Linguagem (**`scopeconfig`**), Expressões Permitidas (**`allowed_patterns` Vault**), **`custom_patterns`** e **`threshold`**.
- [[talisman-modo-interativo-talisman-interactive-cli-developer-experience]] — Veja também: Talisman Modo Interativo (**`-i` / `TALISMAN_INTERACTIVE=true`**): Fluxo Guiado de Aprovação de Falsos Positivos e Atualização Automática do `.talismanrc`.
- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — Referência cruzada direta com talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push.
- [[gitsecrets-instalacao-hooks-locais-templates-globais-init-templatedir]] — Referência cruzada direta com gitsecrets-instalacao-hooks-locais-templates-globais-init-templatedir.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
