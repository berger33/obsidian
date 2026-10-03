---
id: software.seguranca.tranche07.000623
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/hashcat/hashcat/master/README.md", "https://hashcat.net/wiki/doku.php?id=rule_based_attack", "https://hashcat.net/wiki/doku.php?id=mask_attack"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Hashcat: Linguagem de Regras de Mutação (`-r`, `-j`, `-k`), *Multi-Rules* e Estatísticas de Eficiência (`--debug-mode`)

## Em uma frase
As regras do Hashcat (`rules/*.rule`, conforme documentado na wiki oficial `rule_based_attack`) formam uma minilinguagem de operadores de 1 a 3 caracteres que transformam cada palavra do dicionário (capitalização `c`, *leet speak* `sa@ se3 si1 so0`, sufixos `$2$0$2$6$!`, prefixos `^`, rotação `{`/`}`, duplicação `d`, truncamento `'N` e memória `M`/`4`/`6`).

## Por que importa
Permite pegar um dicionário compacto de apenas 50.000 palavras do idioma português e nomes de produtos da empresa e multiplicá-lo instantaneamente na GPU por 10.000 padrões reais de mutação humana.

## Como funciona
É possível encadear **Multi-Rules** passando `-r regra1.rule -r regra2.rule` (aplicando o produto cartesiano das duas listas de regras em sequência) e usar **`--debug-mode=4` `--debug-file=matched_rules.log`** para gravar exatamente qual palavra base, qual regra e qual senha final quebraram cada hash, gerando inteligência estatística para o relatório de conscientização.

## Exemplo
```bash
# Auditar hashes com regras combinadas e registrar no debug-file exatamente quais regras quebraram senhas reais
hashcat -m 1000 -a 0 -O \
  --debug-mode=4 --debug-file=/cases/audit/effective_rules.log \
  /cases/audit/ntds_hashes.txt \
  /opt/secops/wordlists/ptbr_base.dict \
  -r /usr/share/hashcat/rules/best64.rule
```

## Limites e trade-offs
Conforme documentado na wiki oficial do Hashcat, regras de rejeição de candidatos (`<N`, `>N`, `!X`, `/X`) funcionam quando passadas na linha de comando via **`-j`** ou **`-k`** (filtradas no host), mas são ignoradas em arquivos `-r` processados nos kernels rápidos de GPU.

## Como verificar
Analise as regras mais frequentes em `/cases/audit/effective_rules.log` (`cut -d: -f2 effective_rules.log | sort | uniq -c | sort -nr | head`) para identificar o padrão exato de criação de senhas dos usuários da empresa.

## Conexões
- [[hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg]] — Veja também: Hashcat: Os Modos de Ataque (`-a 0` Wordlist, `-a 1` Combinator, `-a 3` Mask/Brute-Force, `-a 6`/`-a 7` Hybrid e `-a 9` Association).
- [[hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment]] — Veja também: Hashcat: Ataques de Máscara (`-a 3`), *Custom Charsets* (`-1` a `-4`), Arquivos `.hcmask` e Ordenação por **Cadeias de Markov**.
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
