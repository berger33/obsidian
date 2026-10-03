---
id: software.seguranca.tranche03.000290
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/VirusTotal/yara/master/README.md", "https://yara.readthedocs.io/en/stable/writingrules.html", "https://github.com/VirusTotal/yara"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# YARA no Ecossistema DFIR/SOC: integração com `Velociraptor`, `osquery`, `ClamAV`, `LimaCharlie` e curadoria com `YARA-CI` / `YARA Forge`

## Em uma frase
Conforme demonstra a extensa lista *Who's using YARA* no README oficial (`VirusTotal/yara`), o YARA é a linguagem universal de detecção de artefatos suportada nativamente por **Rapid7 Velociraptor** (plugin VQL `yara()`), **osquery** (tabelas `yara` e `yara_events`), **Wazuh**, **ClamAV**, **Cuckoo/CAPE Sandbox**, **Radare2**, **x64dbg**, **LimaCharlie**, **Nextron Thor/Loki** e **MISP**.

## Por que importa
Manter regras YARA escritas manualmente sem testá-las contra um corpus grande de arquivos limpos (*goodware*, como binários padrão do Windows/Linux) é a causa número um de falsos positivos que disparam alertas em massa na frota.

## Como funciona
Conforme recomenda o README oficial, utilize integração contínua para suas regras (como **YARA-CI**, `yr check` / `yr fmt` do YARA-X e coleções curadas e testadas como o **YARA Forge** da Nextron / YARAHQ), validando cada nova regra contra um diretório de binários legítimos antes de distribuí-la para o Velociraptor ou osquery!

## Exemplo
```bash
# Pipeline local de validação de regras YARA: 1) zero hits na pasta de goodware legítimo, 2) hit positivo na amostra de teste:
yara -r ./minhas-regras.yar ./corpus-goodware-limpo/ | tee hits-falso-positivo.txt
test ! -s hits-falso-positivo.txt
yara ./minhas-regras.yar ./corpus-malware-teste/sample1.bin
```

## Limites e trade-offs
Inclua sempre nos metadados (`meta:`) de cada regra corporativa os campos `author`, `date`, `reference` (link do relatório/ticket de incidente) e `hash` (SHA-256 da amostra original que motivou a regra) para preservar a memória institucional do SOC.

## Como verificar
Execute o comando de validação contra `/bin` e `/usr/bin` locais para confirmar taxa zero de falsos positivos.

## Conexões
- [[yarasig-automacao-python-yara-python-yara-x-callbacks-timeout]] — Veja também: YARA Automação em Python (`yara-python` e `yara_x`): compilação em memória, callbacks de `matches` e proteção por `timeout`.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://yara.readthedocs.io/en/stable/writingrules.html) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
