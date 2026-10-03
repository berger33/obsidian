---
id: software.seguranca.tranche03.000287
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

# YARA Execução Avançada na CLI: pré-compilação com `yarac`, variáveis externas (`-d var=valor`) e varredura de Memória de Processos (`yara rules.yar <PID>`)

## Em uma frase
O YARA suporta três recursos operacionais cruciais para resposta a incidentes em campo: **1. Varredura direta da memória RAM de um processo em execução** passando o **`PID`** como alvo (`yara rules.yar 4128`), **2. Pré-compilação de milhares de regras em um único arquivo binário rápido (`yarac`)** e **3. Variáveis Externas (`-d ext_var=...`)** injetadas em tempo de execução!

## Por que importa
Malwares *fileless* ou payloads injetados na memória de um processo legítimo (como `nginx`, `python` ou `svchost.exe`) nunca tocam o disco; varrer apenas o sistema de arquivos não os encontra, mas apontar o YARA para o `PID` do processo varre todos os segmentos de memória virtual mapeados daquele processo!

## Como funciona
Além disso, quando você usa **`yarac`** para pré-compilar seu ruleset (carregado depois com **`yara -C compiled.yarc alvo`**), você elimina o tempo de parsing e compilação do autômato Aho-Corasick em cada host e evita expor o código-fonte em texto claro de regras confidenciais de Threat Intelligence.

## Exemplo
```bash
# 1. Pré-compilando um conjunto de regras com yarac e executando com yara -C (-r recursivo, -s mostra strings):
yarac ./regras-corporativas.yar ./regras.yarc
yara -C -r -s ./regras.yarc /var/www/html

# 2. Escaneando a memória virtual de todos os processos em execução no host Linux:
for pid in $(ls /proc | grep -E '^[0-9]+$'); do
  sudo yara -C ./regras.yarc "$pid" 2>/dev/null
done
```

## Limites e trade-offs
Atenção: arquivos binários gerados pelo `yarac` são vinculados à versão específica do YARA; sempre recompile o arquivo `.yarc` quando atualizar a versão do binário `yara` (ou use `yr compile` no YARA-X).

## Como verificar
Teste compilar uma regra com `yarac` e executá-la com `yara -C` sobre um arquivo e sobre o PID do shell atual (`$$`).

## Conexões
- [[yarasig-private-rules-global-rules-tags-anonymous-strings-modularizacao]] — Veja também: YARA Organização Modular de Rulesets: `private rule`, `global rule`, Strings Anônimas (`$`) e `include`.
- [[yarasig-otimizacao-performance-atoms-aho-corasick-regex-bounded-profiling]] — Veja também: YARA Engenharia de Performance: escolha de *Atoms* para o motor Aho-Corasick, perigos de Regex abertas (`.*`) e `short-circuit`.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://yara.readthedocs.io/en/stable/writingrules.html) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
