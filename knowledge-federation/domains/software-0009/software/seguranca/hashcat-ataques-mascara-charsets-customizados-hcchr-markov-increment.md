---
id: software.seguranca.tranche07.000624
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

# Hashcat: Ataques de Máscara (`-a 3`), *Custom Charsets* (`-1` a `-4`), Arquivos `.hcmask` e Ordenação por **Cadeias de Markov**

## Em uma frase
No modo **`-a 3` (Mask Attack)**, o Hashcat substitui a força bruta cega por máscaras posicionais construídas com os conjuntos de caracteres nativos (`?l` minúsculas, `?u` maiúsculas, `?d` dígitos, `?s` símbolos, `?a` todos os imprimíveis ASCII, `?b` bytes `0x00–0xff`) e até **4 conjuntos customizados (`-1`, `-2`, `-3`, `-4`)**.

## Por que importa
Se a política de senhas de uma aplicação exige 8 caracteres começando por letra maiúscula e terminando em 2 dígitos e 1 símbolo comum, testar `?a?a?a?a?a?a?a?a` (`95^8 = 6,6 quadrilhões` de combinações) levaria semanas, enquanto a máscara `-1 '!@#$%&*' ?u?l?l?l?l?d?d?1` (`26 * 26^4 * 100 * 7 = 8,3 bilhões`) termina em **menos de 1 segundo** em uma única GPU moderna.

## Como funciona
Além disso, o Hashcat ordena automaticamente o espaço de busca de cada posição usando **Cadeias de Markov** (`hashcat.hcstat2`), testando primeiro as combinações de letras estatisticamente mais frequentes na língua humana, e suporta **arquivos `.hcmask`** (uma máscara por linha) e incremento de comprimento (`--increment --increment-min 8 --increment-max 10`).

## Exemplo
```bash
# Definir charsets customizados (-1 vogais/consoantes comuns, -2 simbolos corporativos) e testar padrao de 9 caracteres
hashcat -m 1000 -a 3 -O -w 3 \
  -1 "?l?d" -2 "!@#$%&*" \
  /cases/audit/ntds_hashes.txt \
  "?u?l?l?l?1?1?d?d?2"
```

## Limites e trade-offs
Para auditar senhas contendo caracteres acentuados em português (`ç`, `ã`, `é`, `ê`, `ó`) codificados em UTF-8 ou ISO-8859-1, passe um arquivo de charset `.hcchr` (ou `--hex-charset`) em `-1`.

## Como verificar
Comprove ao time de gestão de identidade como requisitos previsíveis de composição de senha reduzem drasticamente a entropia frente a *passphrases* longas de 15+ caracteres.

## Conexões
- [[hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras]] — Veja também: Hashcat: Linguagem de Regras de Mutação (`-r`, `-j`, `-k`), *Multi-Rules* e Estatísticas de Eficiência (`--debug-mode`).
- [[hashcat-auditoria-active-directory-ntds-kerberoasting-asrep-dcc2]] — Veja também: Hashcat: Modos de Hash para Auditoria de Active Directory (`-m 1000` NTLM, `-m 3000` LM, `-m 5600` NetNTLMv2, `-m 13100`/`19700` Kerberoast, `-m 18200` AS-REP e `-m 2100` DCC2).
- [[hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg]] — Referência cruzada direta com hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg.
- [[hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases]] — Referência cruzada direta com hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
