---
id: software.seguranca.tranche03.000282
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
fontes: ["https://yara.readthedocs.io/en/stable/writingrules.html", "https://raw.githubusercontent.com/VirusTotal/yara/master/README.md", "https://github.com/VirusTotal/yara"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# YARA Hexadecimal Strings (`{ ... }`): uso de *nibble wildcards* (`?`), operador *not* (`~`), *jumps* (`[X-Y]`) e alternativas (`( A | B )`)

## Em uma frase
Conforme detalhado na seção *Hexadecimal strings* da documentação oficial (`yara.readthedocs.io/en/stable/writingrules.html`), as strings hexadecimais do YARA (`$hex = { ... }`) permitem casar sequências brutas de bytes e sequências de opcodes de assembly usando quatro construções flexíveis: **1. Wildcards por nibble (`?`)**, **2. Operador de negação (`~`, introduzido no YARA 4.3.0)**, **3. Jumps de comprimento variável (`[X-Y]`)** e **4. Alternativas (`( A | B | C )`)**!

## Por que importa
Quando um compilador gera código de máquina para a mesma função de descriptografia de um malware, os registradores ou deslocamentos de memória (*offsets* de 4 bytes) mudam a cada build, enquanto os opcodes das instruções permanecem os mesmos.

## Como funciona
Usando *nibble wildcards* (`E2 34 ?? C8 A? FB`), negação de byte/nibble (`~00` para casar qualquer byte exceto zero!) e *jumps* limitados (`F4 23 [4-8] 62 B4`), sua assinatura de opcodes ignora os offsets variáveis do compilador e captura todas as variantes da família!

## Exemplo
```yara
rule Opcode_Decryption_Loop_Example
{
    strings:
        // Casa opcodes com wildcard de nibble (?), byte não-nulo (~00), salto de 4 a 6 bytes e alternativas:
        $decrypt_stub = { 48 31 ?? ~00 ( 8A 04 08 | 8A 1C 08 ) [4-6] 48 FF C1 75 ?? }

    condition:
        $decrypt_stub
}
```

## Limites e trade-offs
Para performance máxima do motor Aho-Corasick (que extrai um *atom* de até 4 bytes fixos de cada padrão para busca rápida), comece ou inclua sempre uma sequência de pelo menos 3 a 4 bytes fixos contíguos sem wildcards nem jumps na sua string hexadecimal!

## Como verificar
Compile a regra e verifique avisos de performance de átomos curtos com `yara -w rule.yar sample.bin` (ou `yr check` no YARA-X).

## Conexões
- [[yarasig-arquitetura-virustotal-yara-yara-x-anatomia-regras-meta-strings-condition]] — Veja também: VirusTotal YARA e YARA-X: arquitetura do motor de *Pattern Matching* para pesquisa de malware e anatomia de regras (`meta`, `strings`, `condition`).
- [[yarasig-text-strings-modificadores-nocase-wide-ascii-xor-base64-fullword]] — Veja também: YARA Text Strings e Modificadores de Ofuscação: `nocase`, `wide`, `ascii`, `fullword`, `xor(min-max)`, `base64` e `base64wide`.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://yara.readthedocs.io/en/stable/writingrules.html) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
