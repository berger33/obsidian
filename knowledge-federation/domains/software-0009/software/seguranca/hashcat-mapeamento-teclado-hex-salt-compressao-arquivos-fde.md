---
id: software.seguranca.tranche07.000629
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

# Hashcat: Mapeamento de Layout de Teclado (`--keyboard-layout-mapping`), `--hex-salt` e Leitura Transparente de Wordlists Comprimidas (`.gz`, `.xz`, `.zst`)

## Em uma frase
Conforme documentado em `docs/keyboard-layout-mapping.md` e `docs/hashcat-compression-libraries.md`, o Hashcat inclui suporte nativo para **mapeamento de layouts de teclado internacionais** (`--keyboard-layout-mapping`, essencial para criptografia de disco completo *FDE* como LUKS, BitLocker e VeraCrypt) e descompressão transparente em streaming de dicionários `.gz`, `.xz`, `.zst` e `.7z`.

## Por que importa
Em sistemas com criptografia de disco completo (LUKS/BitLocker), a senha digitada na tela de pré-boot (BIOS/UEFI/GRUB) é frequentemente lida no layout **US-ANSI padrão**, enquanto após o boot do sistema operacional o usuário digita a mesma sequência física de teclas em um teclado **ABNT2 / DE / FR / ES**: o arquivo `.hckmap` traduz os códigos de tecla entre os dois layouts em tempo real.

## Como funciona
Adicionalmente, as flags **`--hex-salt`** e **`--hex-charset`** permitem auditar hashes cujos salts ou senhas contêm bytes binários brutos não-ASCII.

## Exemplo
```bash
# Auditar hash aplicando traducao de layout de teclado e lendo wordlist comprimida em Zstandard (.zst) diretamente
hashcat -m 1000 -a 0 \
  --keyboard-layout-mapping /usr/share/hashcat/layouts/us_to_de.hckmap \
  /cases/audit/target.hash \
  /opt/secops/wordlists/rockyou2024.txt.zst
```

## Limites e trade-offs
Manter grandes dicionários de auditoria comprimidos em **Zstandard (`.zst`)** economiza até 70% de espaço em disco NVMe e é descomprimido em tempo real pelo Hashcat sem perda perceptível de performance.

## Como verificar
Verifique com `ls -lh /usr/share/hashcat/layouts/` os mapas de teclado disponíveis na instalação.

## Conexões
- [[hashcat-ataques-pcfg-probabilistic-context-free-grammar-slow-candidates]] — Veja também: Hashcat: Geração Gramatical com **PCFG (*Probabilistic Context-Free Grammar*)** e Modo **`--slow-candidates` (`-S`)**.
- [[hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases]] — Veja também: Defesa Contra Quebra Offline em GPU: Engenharia de Armazenamento de Senhas com **Argon2id (RFC 9106)**, `bcrypt`/`scrypt`, *Pepper* em HSM/KMS e *Passphrases*.
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.
- [[hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment]] — Referência cruzada direta com hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment.
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
