---
id: software.seguranca.tranche07.000630
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

# Defesa Contra Quebra Offline em GPU: Engenharia de Armazenamento de Senhas com **Argon2id (RFC 9106)**, `bcrypt`/`scrypt`, *Pepper* em HSM/KMS e *Passphrases*

## Em uma frase
A conclusão arquitetural de qualquer auditoria com o Hashcat é que funções de hash criptográficas rápidas (MD4/NTLM, MD5, SHA-1, SHA-256, SHA-512, mesmo com salt único) são totalmente inadequadas para armazenar senhas, pois uma única placa de vídeo avalia dezenas de bilhões de candidatos por segundo.

## Por que importa
Para neutralizar o paralelismo massivo de GPUs e ASICs, o padrão atual recomendado pelo **IETF RFC 9106** e pelo **OWASP Password Storage Cheat Sheet** é uma função de derivação de chave *Memory-Hard* (**`Argon2id`**), que exige alocar blocos grandes de memória RAM por tentativa (ex.: `m=65536` [64 MiB] ou `m=19456` [19 MiB], `t=2` ou `3` iterações, `p=1` paralelismo), esgotando a memória interna dos núcleos de GPU.

## Como funciona
Em conjunto com `Argon2id` (ou `bcrypt` com custo `>= 12` / `PBKDF2-HMAC-SHA256` `>= 600.000` iterações + **HMAC Pepper** armazenado em cofre KMS/HSM separado do banco de dados), políticas modernas de identidade (NIST SP 800-63B) substituem regras artificiais de troca periódica por **Passphrases longas (>= 15 caracteres)**, verificação automática contra listas de senhas vazadas (*Have I Been Pwned* / `k-anonymity` API) e **MFA resistente a phishing (FIDO2 / WebAuthn Passkeys)**.

## Exemplo
```python
# Implementacao de referencia em Python (argon2-cffi) seguindo os parametros de seguranca do RFC 9106 / OWASP
from argon2 import PasswordHasher, Type

ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,  # 64 MiB de RAM por verificacao (Memory-Hard contra GPUs)
    parallelism=2,
    hash_len=32,
    salt_len=16,
    type=Type.ID        # Argon2id (hibrido resistente a side-channel e GPU cracking)
)
hashed = ph.hash(" Frase-De-Passagem-Corporativa-Forte-2026 ")
assert ph.verify(hashed, " Frase-De-Passagem-Corporativa-Forte-2026 ")
```

## Limites e trade-offs
Nunca trunque senhas de usuários em 72 bytes sem pré-hashing seguro (limitação clássica do `bcrypt`) nem proíba espaços ou frases longas nos formulários de cadastro da aplicação.

## Como verificar
Audite o código da aplicação verificando que senhas são armazenadas com `$argon2id$v=19$m=...` e que nenhum hash rápido sem KDF (`MD5`, `SHA1`, `SHA256`) é utilizado para credenciais.

## Conexões
- [[hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde]] — Veja também: Hashcat: Mapeamento de Layout de Teclado (`--keyboard-layout-mapping`), `--hex-salt` e Leitura Transparente de Wordlists Comprimidas (`.gz`, `.xz`, `.zst`).
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.
- [[hashcat-ataques-pcfg-probabilistic-context-free-grammar-slow-candidates]] — Referência cruzada direta com hashcat-ataques-pcfg-probabilistic-context-free-grammar-slow-candidates.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
