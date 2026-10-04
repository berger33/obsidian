---
id: software.seguranca.tranche10.000966
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

# Talisman em **CI/CD e Auditoria de Repositórios**: Varredura Completa de Histórico Git (**`--scan`**), **`--ignoreHistory`**, **`--pattern`** e Relatórios HTML (`--scanWithHtml`)

## Em uma frase
Como alerta o aviso oficial do Talisman, um hook local na máquina do desenvolvedor pode ser contornado com `git commit --no-verify` ou `git push --force` (ou o desenvolvedor pode ter esquecido de instalar o hook). Por isso, toda proteção de estação de trabalho **deve ser acompanhada por uma varredura obrigatória no servidor de CI/CD**!

## Por que importa
Executado como utilitário CLI com a flag **`-s` / `--scan`**, o Talisman percorre **todo o histórico de commits do repositório Git** em busca de segredos que tenham sido introduzidos em qualquer revisão passada e grava relatórios JSON detalhados na pasta **`talisman_reports/`** (ou no caminho especificado por **`-r` / `--reportdirectory`**)!

## Como funciona
Quando você quer varrer no CI/CD apenas os arquivos presentes no `HEAD` atual sem percorrer anos de histórico antigo, adicione **`--ignoreHistory`**; quando quiser varrer arquivos por padrão glob fora de hooks Git, use **`-p` / `--pattern "./config/**/*.yaml"`**; e para gerar um painel visual navegável para a equipe, use **`-w` / `--scanWithHtml`**!

## Exemplo
```bash
# Varrer todo o historico de commits de um repositorio Git (-s / --scan) salvando o relatorio JSON em um diretorio de auditoria
talisman --scan --reportdirectory=/cases/appsec/talisman_audit_reports
```

## Limites e trade-offs
Observe uma diferença importante documentada no `README.md` para o modo `--scan` de histórico: diferentemente do modo `--githook`, o comando `talisman --scan` audita **inclusive os arquivos listados no `.talismanrc`**, garantindo que uma auditoria completa de histórico antes de tornar um repositório privado em Open-Source revele absolutamente tudo!

## Como verificar
Inspecione o arquivo `talisman_reports/data/report.json` com `jq` nos pipelines de CI/CD para falhar o build se houver achados.

## Conexões
- [[talisman-modo-interativo-talisman-interactive-cli-developer-experience]] — Veja também: Talisman Modo Interativo (**`-i` / `TALISMAN_INTERACTIVE=true`**): Fluxo Guiado de Aprovação de Falsos Positivos e Atualização Automática do `.talismanrc`.
- [[talisman-anatomia-detectores-entropia-base64-hex-creditcard-filesize]] — Veja também: Por Dentro dos Detectores do Talisman: Cálculo de **Entropia de Shannon**, Decodificação Recursiva **Base64/Hex**, Cartões de Crédito e Limite de Tamanho.
- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — Referência cruzada direta com talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
