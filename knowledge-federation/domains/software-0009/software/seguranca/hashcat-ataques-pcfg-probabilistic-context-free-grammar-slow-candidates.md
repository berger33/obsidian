---
id: software.seguranca.tranche07.000628
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

# Hashcat: Geração Gramatical com **PCFG (*Probabilistic Context-Free Grammar*)** e Modo **`--slow-candidates` (`-S`)**

## Em uma frase
Para hashes lentos com alto fator de trabalho (como `bcrypt` `-m 3200`, `Argon2` `-m 34000`, `scrypt`, `LUKS` ou `BitLocker`), onde a GPU avalia poucos milhares de candidatos por segundo, a qualidade de cada candidato importa muito mais do que a velocidade bruta de geração; o Hashcat suporta geradores gramaticais **PCFG** (`docs/hashcat-pcfg.md`) e o modo **`-S` (`--slow-candidates`)**.

## Por que importa
Um gerador **PCFG** decompõe senhas reais em estruturas sintáticas probabilísticas (ex.: `Alpha6 + Digits4 + Punct1`, como `Brasil2026!`) e emite os candidatos em ordem estritamente decrescente de probabilidade estatística.

## Como funciona
Quando se utiliza `-S` (`--slow-candidates`) ou se alimenta o Hashcat via `stdin` a partir de um gerador externo (`pcfg_guesser | hashcat -m 3200 ...`), os candidatos são gerados na CPU permitindo usar regras completas e geradores inteligentes sem desperdiçar ciclos de GPU em candidatos improváveis.

## Exemplo
```bash
# Utilizar a flag -S (--slow-candidates) para maximizar a qualidade das regras contra hashes lentos bcrypt (-m 3200)
hashcat -m 3200 -a 0 -S -w 3 \
  /cases/audit/webapp_bcrypt.hashes \
  /opt/secops/wordlists/top_100k_ptbr.dict \
  -r /usr/share/hashcat/rules/best64.rule
```

## Limites e trade-offs
Não utilize `-S` (`--slow-candidates`) com hashes rápidos como NTLM (`-m 1000`) ou MD5 (`-m 0`), pois a geração em CPU limitará severamente o throughput da GPU; reserve `-S` exclusivamente para algoritmos lentos de KDF (`bcrypt`, `Argon2`, `PBKDF2`, `DCC2`, `WPA-PBKDF2`).

## Como verificar
Monitore a linha `Speed.#1` no status interativo (`s`) do Hashcat para confirmar que as GPUs permanecem em 99–100% de utilização.

## Conexões
- [[hashcat-extensibilidade-assimilation-bridge-plugins-python-rust-c]] — Veja também: Hashcat v7+: **Assimilation Bridge** para Criação de Novos Modos de Hash em **Python, Rust ou C** sem Escrever Kernels GPU.
- [[hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde]] — Veja também: Hashcat: Mapeamento de Layout de Teclado (`--keyboard-layout-mapping`), `--hex-salt` e Leitura Transparente de Wordlists Comprimidas (`.gz`, `.xz`, `.zst`).
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.
- [[hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras]] — Referência cruzada direta com hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras.
- [[hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases]] — Referência cruzada direta com hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
