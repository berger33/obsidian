---
id: software.seguranca.tranche10.000965
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

# Talisman Modo Interativo (**`-i` / `TALISMAN_INTERACTIVE=true`**): Fluxo Guiado de Aprovação de Falsos Positivos e Atualização Automática do `.talismanrc`

## Em uma frase
Uma das principais razões pelas quais desenvolvedores usam `git commit --no-verify` (pulando os hooks de segurança!) é a fricção operacional quando um falso positivo legítimo (como um certificado público de teste ou um arquivo de fixture) é bloqueado e exige copiar e colar manualmente blocos YAML e hashes SHA-256 no `.talismanrc`.

## Por que importa
O Talisman resolve essa fricção com o **Modo Interativo (`-i` / `--interactive` ou variável de ambiente `export TALISMAN_INTERACTIVE=true`)**!

## Como funciona
Quando `TALISMAN_INTERACTIVE=true` está ativo no terminal (Linux/macOS) ou você executa **`talisman -i -g pre-commit`**, sempre que um arquivo aciona um alerta, o próprio Talisman exibe o motivo do bloqueio e pergunta interativamente no prompt se você confirmou que o arquivo não contém segredos e deseja **adicionar automaticamente a entrada com o `checksum` SHA-256 calculado diretamente no `.talismanrc`**!

## Exemplo
```bash
# Executar o Talisman em modo interativo sobre o changeset pre-commit para revisar alertas e atualizar o .talismanrc passo a passo
export TALISMAN_INTERACTIVE=true
talisman --interactive --githook pre-commit
```

## Limites e trade-offs
Atenção a uma limitação técnica documentada no `README.md` oficial: se o desenvolvedor fizer o commit clicando no botão gráfico de Version Control dentro de uma IDE (VS Code, IntelliJ, Goland) que não aloca um TTY interativo para o hook Git, o prompt interativo não poderá receber entrada do teclado; nesse caso, o desenvolvedor pode rodar `talisman -i -g pre-commit` no terminal integrado da IDE.

## Como verificar
Instrua a equipe nos treinamentos de AppSec a nunca confirmar `[y]` no modo interativo sem antes ler a linha exata destacada pelo relatório do Talisman.

## Conexões
- [[talisman-instalacao-global-git-template-framework-pre-commit-husky]] — Veja também: Talisman em Escala de Engenharia: Instalação via **Global Git Hook Template (`init.templateDir`)**, Framework **`pre-commit`** e **Husky**.
- [[talisman-varredura-historico-git-scan-reportdirectory-scanwithhtml]] — Veja também: Talisman em **CI/CD e Auditoria de Repositórios**: Varredura Completa de Histórico Git (**`--scan`**), **`--ignoreHistory`**, **`--pattern`** e Relatórios HTML (`--scanWithHtml`).
- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — Referência cruzada direta com talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push.
- [[talisman-governanca-checksum-sha256-talismanrc-ignore-detectors]] — Referência cruzada direta com talisman-governanca-checksum-sha256-talismanrc-ignore-detectors.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
