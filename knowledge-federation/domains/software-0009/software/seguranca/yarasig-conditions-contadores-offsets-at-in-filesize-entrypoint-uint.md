---
id: software.seguranca.tranche03.000284
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

# YARA Expressões em `condition`: contadores (`#a`), offsets (`@a[i]`), `at`, `in`, `of them`, `filesize` e leitura de inteiros (`uint16`, `uint32`)

## Em uma frase
A seção **`condition:`** do YARA é uma linguagem de expressões completa que permite combinar operadores booleanos (`and`, `or`, `not`), operadores relacionais e bit-a-bit, **contagem de ocorrências de uma string (`#a > 5`)**, **offset exato da i-ésima ocorrência (`@a[1] < 1024`)**, comprimento do match (`!a[1]`), operadores de posição (`$a at 0`, `$a in (0..4096)`), conjuntos (`2 of ($s*)`, `all of them`, `any of ($a, $b, $c)`) e leitura direta de inteiros little-endian/big-endian do arquivo (**`uint16(0) == 0x5A4D`**, **`uint32(uint32(0x3C)) == 0x00004550`**)!

## Por que importa
Verificar `uint16(0) == 0x5A4D` (assinatura `"MZ"` de um executável Windows PE) e `filesize < 10MB` antes de avaliar expressões complexas ou módulos pesados permite descartar 99% dos arquivos irrelevantes (como vídeos, imagens ou logs de gigabytes) em nanosegundos!

## Como funciona
Você também pode usar laços **`for any i in (1..#a) : (@a[i] < @b[1])`** para verificar a ordem relativa em que duas strings ou estruturas aparecem dentro do binário.

## Exemplo
```yara
rule Fast_PE_Header_And_String_Count_Check
{
    strings:
        $s1 = "CreateRemoteThread" ascii fullword
        $s2 = "WriteProcessMemory" ascii fullword
        $s3 = "OpenProcess" ascii fullword
        $nop_sled = { 90 90 90 90 90 90 90 90 }

    condition:
        // Verifica magic MZ (0x5A4D) no offset 0, assinatura PE\0\0 (0x00004550) no offset apontado por 0x3C:
        uint16(0) == 0x5A4D and
        uint32(uint32(0x3C)) == 0x00004550 and
        filesize < 8MB and
        (all of ($s*) or #nop_sled > 10)
}
```

## Limites e trade-offs
Lembre-se de que os inteiros `uint16(offset)` e `uint32(offset)` no YARA são **little-endian** por padrão: por isso os bytes ASCII `"MZ"` (`0x4D`, `0x5A`) são lidos como **`0x5A4D`**! Para leitura big-endian (ex.: cabeçalho ELF ou classes Java `0xCAFEBABE`), use **`uint32be(0)`**.

## Como verificar
Teste a condição acima contra binários PE e arquivos de texto confirmando a filtragem instantânea pelo cabeçalho.

## Conexões
- [[yarasig-text-strings-modificadores-nocase-wide-ascii-xor-base64-fullword]] — Veja também: YARA Text Strings e Modificadores de Ofuscação: `nocase`, `wide`, `ascii`, `fullword`, `xor(min-max)`, `base64` e `base64wide`.
- [[yarasig-modulos-pe-elf-math-hash-cuckoo-dotnet-inspecao-estrutural]] — Veja também: YARA Módulos Embutidos (`import "pe"`, `"elf"`, `"math"`, `"hash"`, `"dotnet"`): inspeção de imports, seções, entropia, imphash e assinaturas Authenticode.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://yara.readthedocs.io/en/stable/writingrules.html) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
