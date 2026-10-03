---
id: software.seguranca.tranche03.000288
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

# YARA Engenharia de Performance: escolha de *Atoms* para o motor Aho-Corasick, perigos de Regex abertas (`.*`) e `short-circuit`

## Em uma frase
Para que um ruleset com 5.000 regras YARA consiga varrer gigabytes de disco ou memória em poucos segundos sem travar a CPU, o autor de regras precisa compreender como funciona o motor interno de duas fases do YARA: **Fase 1 — busca simultânea de *Atoms* (substrings curtas de até 4 bytes extraídas de cada padrão) pelo autômato Aho-Corasick**, seguida pela **Fase 2 — verificação completa do padrão e avaliação do bytecode da `condition`**.

## Por que importa
Se você escrever uma expressão regular que começa com quantificador aberto (`/http:\/\/.*\/gate\.php/`) ou uma string curta muito comum (`$a = "00"` ou `{ 00 00 00 00 }`), o YARA não conseguirá extrair um átomo seletivo de 4 bytes: o Aho-Corasick acionará o verificador de regex milhões de vezes por arquivo (*"rule is slowing down scanning"*), derrubando a performance em 1.000x!

## Como funciona
Siga três regras de ouro de performance YARA: 1) nunca use `.*` ou `.+` ilimitados em regexes — use quantificadores limitados como `.{1,64}` e ancore em literais específicos; 2) evite strings de menos de 4 bytes ou sequências repetitivas (`00 00 00 00`, `FF FF FF FF`); e 3) use `yr check` (YARA-X) ou `yara` com avisos habilitados para detectar regras lentas no CI!

## Exemplo
```yara
rule High_Performance_Regex_Design
{
    strings:
        // RUIM (sem átomo de 4 bytes seletivo e .* ilimitado): /https?:\/\/.*\/login\.php/
        // BOM (átomo literal "/api/v2/beacon" de alta seletividade e quantificador limitado):
        $fast_uri = /\/api\/v2\/beacon\/[a-f0-9]{16,32}\/status/ ascii

    condition:
        filesize < 5MB and $fast_uri
}
```

## Limites e trade-offs
Se você realmente precisar verificar se um byte ou sequência comum como `{ 00 00 00 00 }` está em uma posição específica (ex.: offset `0x40`), **não defina uma string na seção `strings:`**: use **`uint32(0x40) == 0x00000000`** diretamente na seção `condition:`, o que não polui o autômato Aho-Corasick!

## Como verificar
Audite a qualidade e velocidade das suas regras com `yara -w` ou `yr check` antes de promovê-las para os agentes de endpoint.

## Conexões
- [[yarasig-compilacao-binaria-yarac-external-variables-d-varredura-processos-pid]] — Veja também: YARA Execução Avançada na CLI: pré-compilação com `yarac`, variáveis externas (`-d var=valor`) e varredura de Memória de Processos (`yara rules.yar <PID>`).
- [[yarasig-automacao-python-yara-python-yara-x-callbacks-timeout]] — Veja também: YARA Automação em Python (`yara-python` e `yara_x`): compilação em memória, callbacks de `matches` e proteção por `timeout`.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://yara.readthedocs.io/en/stable/writingrules.html) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
