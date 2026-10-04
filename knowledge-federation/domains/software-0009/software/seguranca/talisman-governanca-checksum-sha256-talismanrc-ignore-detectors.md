---
id: software.seguranca.tranche10.000962
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

# Talisman **`.talismanrc` & Checksum SHA-256 (`--checksum`)**: Por Que o Modelo de **Exceção Vinculada ao Hash** Impede Vazamentos Futuros em Arquivos Ignorados

## Em uma frase
Qual é o maior perigo de segurança na maioria dos scanners de segredos tradicionais quando um desenvolvedor adiciona o caminho `config/app-settings.yaml` em um arquivo `.ignore` comum por causa de um falso positivo? Uma vez que `config/app-settings.yaml` está na lista de ignorados, **aquele arquivo fica cego para sempre** — se 6 meses depois outro desenvolvedor colar uma chave privada real da AWS dentro de `config/app-settings.yaml`, o scanner ignorará o arquivo silenciosamente!

## Por que importa
O **Talisman** resolve essa falha estrutural com um design brilhante no arquivo **`.talismanrc`**: para ignorar um arquivo em `fileignoreconfig:`, o Talisman exige o **Hash Criptográfico SHA-256 coletivo (`checksum:`) daquele arquivo exato no momento da aprovação**!

## Como funciona
Enquanto o arquivo `config/app-settings.yaml` permanecer idêntico, o `checksum` bate e o Talisman não incomoda a equipe; **mas no instante em que qualquer linha de `config/app-settings.yaml` for modificada em um commit futuro, o SHA-256 muda, invalida a exceção automaticamente e força o Talisman a re-escanear o arquivo em busca de novos segredos**!

## Exemplo
```bash
# Calcular o checksum SHA-256 exigido pelo .talismanrc para arquivos especificos ou padroes glob (--checksum)
talisman --checksum="certs/public-test-ca.pem *.lock"
```

## Limites e trade-offs
Melhor ainda: caso apenas o **nome** do arquivo dispare um falso positivo (por exemplo, um script chamado `rotate-ssh-keys.sh` que aciona o detector `filename`, mas cujo conteúdo não deve deixar de ser inspecionado!), use **`ignore_detectors: [filename]`** no `.talismanrc` — mantendo os detectores `filecontent`, `entropy` e `encoded` 100% ativos sobre aquele arquivo!

## Como verificar
Sempre audite mudanças no arquivo `.talismanrc` em Pull Requests via `CODEOWNERS` da equipe de AppSec.

## Conexões
- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — Veja também: **Thoughtworks Talisman (`thoughtworks/talisman`)**: Arquitetura dos **6 Detectores de Segredos** em Hooks Git (**`pre-commit` vs `pre-push`**).
- [[talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity]] — Veja também: Talisman `.talismanrc`: Escopos de Linguagem (**`scopeconfig`**), Expressões Permitidas (**`allowed_patterns` Vault**), **`custom_patterns`** e **`threshold`**.
- [[kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id]] — Referência cruzada direta com kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
