---
id: software.seguranca.tranche03.000283
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

# YARA Text Strings e Modificadores de Ofuscação: `nocase`, `wide`, `ascii`, `fullword`, `xor(min-max)`, `base64` e `base64wide`

## Em uma frase
Na seção *Text strings* de `writingrules.html`, o YARA fornece modificadores nativos que encontram strings textuais mesmo quando o autor do malware tenta escondê-las com codificações diferentes: **`ascii`** (padrão, 1 byte por caractere), **`wide`** (UTF-16LE, 2 bytes por caractere com `0x00` intercalado, padrão da API Win32), **`nocase`** (case-insensitive), **`fullword`** (delimitada por caracteres não-alfanuméricos), **`xor`** (busca a string cifrada com todas as 255 chaves XOR de 1 byte!) e **`base64` / `base64wide`** (busca todas as 3 permutações de alinhamento Base64 da string, inclusive com alfabeto customizado)!

## Por que importa
Autores de malware raramente deixam a URL do servidor C2 ou `"powershell.exe"` em ASCII limpo no binário: eles aplicam um XOR de 1 byte sobre as strings ou as codificam em Base64 (ou Base64 de uma string UTF-16LE `wide`, como faz o `powershell -EncodedCommand`).

## Como funciona
Adicionando simplesmente **`xor(0x01-0xff)`** ou **`base64` / `base64wide`** ao final da definição da string, o compilador do YARA gera automaticamente todas as variações em tempo de compilação e encontra a string ofuscada sem precisar descriptografar o binário antes!

## Exemplo
```yara
rule Detect_Obfuscated_PowerShell_And_XOR_Strings
{
    strings:
        $ps_cmd = "Invoke-Expression" ascii wide nocase base64 base64wide
        $c2_xor = "http://c2.malicious.example/gate.php" ascii wide xor(0x01-0xff)
        $api_name = "VirtualAllocEx" ascii fullword

    condition:
        $api_name and ($ps_cmd or $c2_xor)
}
```

## Limites e trade-offs
Ao usar o modificador **`xor`**, especifique o intervalo **`xor(0x01-0xff)`** quando você não quiser que a regra case com a string em texto plano (`0x00`), ou use `xor` simples para casar tanto em texto plano (`0x00`) quanto com chaves `0x01..0xff`.

## Como verificar
Para saber exatamente qual chave XOR foi encontrada no arquivo durante o match, passe a flag **`-s` (`--print-strings`)** e **`-X` (`--print-xor-key`)** na CLI do `yara`!

## Conexões
- [[yarasig-hexadecimal-strings-wildcards-not-jumps-alternatives]] — Veja também: YARA Hexadecimal Strings (`{ ... }`): uso de *nibble wildcards* (`?`), operador *not* (`~`), *jumps* (`[X-Y]`) e alternativas (`( A | B )`).
- [[yarasig-conditions-contadores-offsets-at-in-filesize-entrypoint-uint]] — Veja também: YARA Expressões em `condition`: contadores (`#a`), offsets (`@a[i]`), `at`, `in`, `of them`, `filesize` e leitura de inteiros (`uint16`, `uint32`).

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://yara.readthedocs.io/en/stable/writingrules.html) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
