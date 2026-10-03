---
id: software.seguranca.tranche10.000967
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

# Por Dentro dos Detectores do Talisman: Cálculo de **Entropia de Shannon**, Decodificação Recursiva **Base64/Hex**, Cartões de Crédito e Limite de Tamanho

## Em uma frase
Por que o Talisman consegue capturar segredos customizados que não seguem um prefixo fixo conhecido (como uma senha aleatória de 40 caracteres gerada para o banco PostgreSQL ou uma chave mestra AES-256 codificada em Base64 ou Hexadecimal)?

## Por que importa
Porque além do detector de palavras-chave e padrões (`FileContentDetector`), o motor do Talisman aplica três detectores agnósticos de formato: **(1) `Entropy`** — divide strings longas e calcula a incerteza estatística (entropia) dos caracteres; **(2) `Base64Content` e `HexContent`** — identifica literais longos que formam cadeias Base64 ou Hexadecimais válidas e verifica se o conteúdo codificado apresenta alta aleatoriedade típica de chaves criptográficas; e **(3) `FileSizeDetector`** — bloqueia o commit de arquivos acima do limite padrão (ex.: dumps `.sql` ou pacotes binários acidentais)!

## Como funciona
Além disso, o **`CreditCardDetector`** identifica sequências numéricas de 13 a 19 dígitos que passam na soma de verificação do **Algoritmo de Luhn** (protegendo contra o commit acidental de PANs reais de cartões de crédito em arquivos de teste — conformidade **PCI DSS**)!

## Exemplo
```bash
# Executar o Talisman com modo de depuracao (-d / --debug) sobre um padrao de arquivos (-p) para inspecionar a pontuacao de cada detector
talisman --debug --pattern="src/config/*.json"
```

## Limites e trade-offs
Se um arquivo de código legítimo contiver constantes hexadecimais inofensivas (como hashes SHA-256 de imagens públicas ou tabelas CRC) que acionam o `HexContent` sem serem segredos, você pode rebaixar apenas a severidade de `HexContent` em `custom_severities:` no `.talismanrc` mantendo `Base64Content` e `FileContent` em alerta máximo.

## Como verificar
Use `--debug` sempre que precisar entender exatamente qual detector interno e qual expressão regular acionou um alerta em um arquivo grande.

## Conexões
- [[talisman-varredura-historico-git-scan-reportdirectory-scanwithhtml]] — Veja também: Talisman em **CI/CD e Auditoria de Repositórios**: Varredura Completa de Histórico Git (**`--scan`**), **`--ignoreHistory`**, **`--pattern`** e Relatórios HTML (`--scanWithHtml`).
- [[talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection]] — Veja também: Governança DevSecOps sobre o `.talismanrc`: Como Impedir que Desenvolvedores Aprovem Vazamentos Reais via **GitHub `CODEOWNERS`** e Auditoria de PR.
- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — Referência cruzada direta com talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push.
- [[talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity]] — Referência cruzada direta com talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
