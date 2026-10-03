---
id: software.seguranca.tranche03.000286
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

# YARA Organização Modular de Rulesets: `private rule`, `global rule`, Strings Anônimas (`$`) e `include`

## Em uma frase
Conforme documentado em `writingrules.html`, para organizar grandes repositórios corporativos de milhares de regras sem duplicação de código, o YARA oferece **`private rule`** (regras auxiliares que nunca são reportadas na saída por conta própria, mas podem ser referenciadas na `condition` de outras regras!), **`global rule`** (regras de pré-condição global que devem ser satisfeitas para que qualquer outra regra do arquivo seja avaliada) e **Strings Anônimas (`$ = "..."` referenciadas via `any of them`)**!

## Por que importa
Se você tem 50 regras para diferentes famílias de Web Shells em PHP e todas precisam verificar primeiro se o arquivo começa com `<?php` e tem menos de 2 MB, repetir essa lógica ou encadear regras com clareza evita erros de manutenção.

## Como funciona
Criando uma **`private rule Is_PHP_File`** (ou usando `private global rule`), todas as suas regras de detecção referenciam `Is_PHP_File and ...` na `condition:`, mantendo a saída do scanner limpa apenas com o nome da regra final que disparou!

## Exemplo
```yara
private rule Is_Small_ELF_Binary
{
    condition:
        uint32be(0) == 0x7F454C46 and filesize < 10MB
}

rule Linux_Backdoor_ReverseShell : linux backdoor
{
    strings:
        $ = "/bin/sh -i" ascii
        $ = "socket" ascii fullword
        $ = "dup2" ascii fullword
        $ = "connect" ascii fullword

    condition:
        Is_Small_ELF_Binary and all of them
}
```

## Limites e trade-offs
Na CLI do `yara`, você pode filtrar a execução para reportar apenas regras que possuam uma **tag** específica (`rule Nome : tag1 tag2`) usando a flag **`-t <tag>` (`--tag=<tag>`)**, por exemplo `yara -t ransomware rules.yar /scan/dir`.

## Como verificar
Teste criar uma `private rule` e confirme que ela não aparece na saída de `yara rules.yar sample`, mas habilita a regra dependente.

## Conexões
- [[yarasig-modulos-pe-elf-math-hash-cuckoo-dotnet-inspecao-estrutural]] — Veja também: YARA Módulos Embutidos (`import "pe"`, `"elf"`, `"math"`, `"hash"`, `"dotnet"`): inspeção de imports, seções, entropia, imphash e assinaturas Authenticode.
- [[yarasig-compilacao-binaria-yarac-external-variables-d-varredura-processos-pid]] — Veja também: YARA Execução Avançada na CLI: pré-compilação com `yarac`, variáveis externas (`-d var=valor`) e varredura de Memória de Processos (`yara rules.yar <PID>`).

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://yara.readthedocs.io/en/stable/writingrules.html) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
