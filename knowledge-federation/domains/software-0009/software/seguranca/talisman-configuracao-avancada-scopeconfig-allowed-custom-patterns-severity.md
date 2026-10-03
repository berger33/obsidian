---
id: software.seguranca.tranche10.000963
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

# Talisman `.talismanrc`: Escopos de Linguagem (**`scopeconfig`**), Expressões Permitidas (**`allowed_patterns` Vault**), **`custom_patterns`** e **`threshold`**

## Em uma frase
Para adaptar o Talisman à realidade de projetos reais em **Go, Node.js, Python ou PHP** sem inundar os desenvolvedores com falsos positivos em arquivos de lock de pacotes (`package-lock.json`, `yarn.lock`, `go.sum`, `composer.lock`, que contêm centenas de hashes Base64/SHA-512 legítimos de integridade de dependências!), o `.talismanrc` oferece a seção **`scopeconfig:`**!

## Por que importa
Basta declarar `scopeconfig: [scope: go, scope: node, scope: images]` e o Talisman ignora automaticamente os artefatos conhecidos daquele ecossistema!

## Como funciona
Além disso, o `.talismanrc` permite: **(1) `allowed_patterns:`** (expressões regulares Go por arquivo ou globais para permitir linhas seguras, como `export AWS_SECRET_ACCESS_KEY=$(vault read ...)` que buscam segredos dinamicamente no HashiCorp Vault em vez de hardcoded!); **(2) `custom_patterns:`** (regexes específicas da sua empresa, tratadas sempre como severidade **`high`**!); e **(3) `threshold: medium`** + **`custom_severities:`** para calibrar o nível de bloqueio!

## Exemplo
```yaml
# .talismanrc — Configuracao corporativa combinando escopos de linguagem, padroes permitidos (Vault) e padroes customizados
version: "1.0"
scopeconfig:
  - scope: go
  - scope: node
  - scope: images
threshold: medium
custom_patterns:
  - "CORP_INTERNAL_TOKEN_[A-Za-z0-9]{32}"
allowed_patterns:
  - "export\\s+AWS_[A-Z_]*=\\$\\(vault\\s+read.*"
custom_severities:
  - detector: HexContent
    severity: low
```

## Limites e trade-offs
Veja como a combinação de `allowed_patterns` para chamadas `$(vault read ...)` ou `op read op://...` incentiva boas práticas: o Talisman bloqueia implacavelmente se alguém escrever `AWS_SECRET_ACCESS_KEY="wJalr..."`, mas permite sem fricção quando o script busca o segredo em tempo de execução de um cofre seguro!

## Como verificar
Evite adicionar `allowed_patterns` genéricos demais no nível global do repositório; prefira declará-los dentro do item específico de `fileignoreconfig` quando a exceção se aplicar a um único arquivo.

## Conexões
- [[talisman-governanca-checksum-sha256-talismanrc-ignore-detectors]] — Veja também: Talisman **`.talismanrc` & Checksum SHA-256 (`--checksum`)**: Por Que o Modelo de **Exceção Vinculada ao Hash** Impede Vazamentos Futuros em Arquivos Ignorados.
- [[talisman-instalacao-global-git-template-framework-pre-commit-husky]] — Veja também: Talisman em Escala de Engenharia: Instalação via **Global Git Hook Template (`init.templateDir`)**, Framework **`pre-commit`** e **Husky**.
- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — Referência cruzada direta com talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push.
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — Referência cruzada direta com gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
