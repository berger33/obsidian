---
id: software.seguranca.tranche07.000622
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

# Hashcat: Os Modos de Ataque (`-a 0` Wordlist, `-a 1` Combinator, `-a 3` Mask/Brute-Force, `-a 6`/`-a 7` Hybrid e `-a 9` Association)

## Em uma frase
O Hashcat estrutura a geração de candidatos através do parâmetro **`-a <modo>` (`--attack-mode`)**, permitindo modelar com precisão matemática os hábitos humanos de criação de senhas corporativas.

## Por que importa
Enquanto a força bruta cega é inviável para senhas longas, usuários corporativos frequentemente combinam duas palavras (`Empresa` + `2026!`) ou seguem o padrão da política do Active Directory (`Maiúscula + 6 minúsculas + 4 dígitos + símbolo`), que é testado em minutos combinando modos híbridos e máscaras.

## Como funciona
Os modos principais são: **`-a 0` Straight / Wordlist** (dicionário puro ou combinado com regras `-r`), **`-a 1` Combination** (concatena cada palavra do `dict1.txt` com cada palavra do `dict2.txt`, aceitando regras individuais `-j` para a esquerda e `-k` para a direita), **`-a 3` Brute-Force / Mask** (expande máscaras posicionais e cadeias de Markov), **`-a 6` Hybrid Wordlist + Mask** (anexa uma máscara ao final de cada palavra do dicionário, ex.: `dict.txt ?d?d?d?s`), **`-a 7` Hybrid Mask + Wordlist** (prefixa uma máscara antes da palavra) e **`-a 9` Association Attack** (*Context-Specific*, onde cada hash é testado contra dicas específicas daquele usuário, como seu `username` ou nome do departamento).

## Exemplo
```bash
# Executar ataque Hibrido (-a 6) anexando 4 digitos e 1 simbolo ao final de cada palavra do dicionario corporativo
hashcat -m 1000 -a 6 -O -w 3 \
  /cases/audit/ntds_hashes.txt \
  /opt/secops/wordlists/corp_terms.dict "?d?d?d?d?s"
```

## Limites e trade-offs
O modo **`-a 9` (Association Attack)** é extremamente eficaz em auditorias de Active Directory para detectar usuários cuja senha contém variações do próprio `sAMAccountName`, nome completo ou cidade sem precisar testar essas strings contra os outros 50.000 hashes do domínio.

## Como verificar
Utilize `--stdout` com uma wordlist pequena (`hashcat -a 6 sample.dict "?d?d" --stdout`) para inspecionar os candidatos gerados antes de iniciar a sessão em GPU.

## Conexões
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Veja também: Hashcat: Arquitetura de Auditoria de Senhas em GPU (Backends CUDA/HIP/Metal/OpenCL), *In-Kernel Rule Engine* e Perfis de Carga (`-w`).
- [[hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras]] — Veja também: Hashcat: Linguagem de Regras de Mutação (`-r`, `-j`, `-k`), *Multi-Rules* e Estatísticas de Eficiência (`--debug-mode`).
- [[hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment]] — Referência cruzada direta com hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
