---
id: software.seguranca.tranche03.000281
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

# VirusTotal YARA e YARA-X: arquitetura do motor de *Pattern Matching* para pesquisa de malware e anatomia de regras (`meta`, `strings`, `condition`)

## Em uma frase
Conforme documentado no README oficial (`VirusTotal/yara`, licenciado sob BSD-3-Clause) e no guia *Writing YARA rules* (`yara.readthedocs.io/en/stable/writingrules.html`), o **YARA** (e seu sucessor moderno reescrito em Rust pelo VirusTotal, o **YARA-X**) é a ferramenta padrão mundial para identificar e classificar amostras de malware e artefatos forenses em arquivos e memória de processos com base em padrões textuais, hexadecimais e expressões booleanas.

## Por que importa
Indicadores simples como hashes SHA-256 identificam apenas um arquivo exato bit-a-bit; já uma regra YARA descreve a estrutura genética de uma família inteira de malware, permanecendo eficaz mesmo quando o invasor recompila o binário ou altera strings secundárias.

## Como funciona
Toda regra YARA inicia com `rule <identificador>` (opcionalmente precedida por modificadores **`private`** ou **`global`** e seguida por `: tag1 tag2`) e divide-se em três seções: **`meta:`** (metadados chave-valor como `author`, `description`, `reference`, `date`, `hash`), **`strings:`** (definição dos padrões `$a`, `$b` a buscar) e **`condition:`** (a expressão lógica booleana obrigatória que determina o disparo da regra)!

## Exemplo
```yara
rule Detect_Linux_Dropper_Example : linux dropper
{
    meta:
        author = "Equipe DFIR / Threat Intel"
        description = "Detecta strings características e magic bytes ELF de dropper customizado"
        severity = "High"

    strings:
        $elf_magic = { 7F 45 4C 46 }
        $cmd_memfd = "memfd_create" ascii fullword
        $c2_marker = "X-Beacon-Session-ID:" ascii nocase

    condition:
        $elf_magic at 0 and filesize < 5MB and ($cmd_memfd and $c2_marker)
}
```

## Limites e trade-offs
Conforme nota oficial no README do `VirusTotal/yara`, a implementação clássica em C entrou em modo de manutenção em favor do **YARA-X** (`VirusTotal/yara-x`, escrito em Rust), que mantém compatibilidade com a linguagem de regras YARA trazendo segurança de memória, mensagens de erro superiores e compilação mais rápida!

## Como verificar
Execute `yara -v` (ou `yr --version` no YARA-X) e teste a regra acima contra um binário com `yara rule.yar /bin/ls`.

## Conexões
- [[yarasig-hexadecimal-strings-wildcards-not-jumps-alternatives]] — Veja também: YARA Hexadecimal Strings (`{ ... }`): uso de *nibble wildcards* (`?`), operador *not* (`~`), *jumps* (`[X-Y]`) e alternativas (`( A | B )`).

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://yara.readthedocs.io/en/stable/writingrules.html) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
