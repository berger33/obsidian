---
id: software.seguranca.tranche03.000285
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

# YARA Módulos Embutidos (`import "pe"`, `"elf"`, `"math"`, `"hash"`, `"dotnet"`): inspeção de imports, seções, entropia, imphash e assinaturas Authenticode

## Em uma frase
Por meio da diretiva **`import "<modulo>"`** no topo do arquivo `.yar`, o YARA estende a seção `condition:` com parsers profundos de formatos executáveis e cálculos matemáticos: **`pe`** (seções, *Import Address Table*, `pe.imphash()`, exports, timestamps, recursos e certificados Authenticode `pe.signatures`), **`elf`** (seções, segmentos, símbolos e `elf.telfhash()`), **`dotnet`** (assemblies C#/.NET, streams e GUIDs), **`math`** (`math.entropy(offset, size)` para detectar binários empacotados/cifrados!) e **`hash`** (`hash.sha256(offset, size)`).

## Por que importa
Empacotadores (*packers* como UPX modificado, Themida ou crypters de ransomware) comprimem ou cifram o código malicioso dentro de uma seção PE com **alta entropia de Shannon (>= 7.2)** e permissão simultânea de escrita e execução (`IMAGE_SCN_MEM_WRITE | IMAGE_SCN_MEM_EXECUTE`), escondendo todas as strings originais.

## Como funciona
Combinando `import "pe"` com `import "math"`, uma regra YARA detecta binários empacotados ou verifica o **`pe.imphash()`** (hash da tabela de funções importadas da API do Windows) sem depender de nenhuma string de texto!

## Exemplo
```yara
import "pe"
import "math"

rule Detect_Packed_PE_With_High_Entropy_RWX_Section
{
    condition:
        pe.is_pe and
        for any section in pe.sections : (
            (section.characteristics & pe.SECTION_MEM_EXECUTE) != 0 and
            (section.characteristics & pe.SECTION_MEM_WRITE) != 0 and
            math.entropy(section.raw_data_offset, section.raw_data_size) >= 7.2
        )
}
```

## Limites e trade-offs
O cálculo de `math.entropy(...)` e `hash.sha256(...)` percorre os bytes do arquivo no momento da avaliação da `condition`; portanto, coloque sempre checagens rápidas (como `pe.is_pe`, `filesize < 10MB` ou presença de strings) **à esquerda do `and`** para aproveitar o *short-circuit evaluation*!

## Como verificar
Execute `yara -D rule.yar sample.exe` (`--print-module-data`) para despejar todos os campos extraídos pelos módulos `pe`/`elf` sobre um arquivo.

## Conexões
- [[yarasig-conditions-contadores-offsets-at-in-filesize-entrypoint-uint]] — Veja também: YARA Expressões em `condition`: contadores (`#a`), offsets (`@a[i]`), `at`, `in`, `of them`, `filesize` e leitura de inteiros (`uint16`, `uint32`).
- [[yarasig-private-rules-global-rules-tags-anonymous-strings-modularizacao]] — Veja também: YARA Organização Modular de Rulesets: `private rule`, `global rule`, Strings Anônimas (`$`) e `include`.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://yara.readthedocs.io/en/stable/writingrules.html) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
