---
id: software.seguranca.tranche07.000627
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

# Hashcat v7+: **Assimilation Bridge** para Criação de Novos Modos de Hash em **Python, Rust ou C** sem Escrever Kernels GPU

## Em uma frase
Introduzido na arquitetura moderna do Hashcat (`docs/hashcat-assimilation-bridge.md`), o **Assimilation Bridge** permite adicionar suporte a esquemas de hash proprietários ou legados escrevendo apenas um módulo simples em **Python**, **Rust** ou **C** no host, sem precisar programar kernels complexos em OpenCL/CUDA.

## Por que importa
Durante pentests de aplicações legadas ou ERPs internos, é comum encontrar esquemas de hash customizados no banco de dados (ex.: `SHA256(salt + MD5(username + password) + pepper)` com codificação Base64 customizada) que não possuem um modo `-m` pré-existente.

## Como funciona
Com o *Assimilation Bridge* (e os modos genéricos de plugin `docs/hashcat-python-plugin-quickstart.md` e `docs/hashcat-rust-plugin-quickstart.md`), a GPU ou o pipeline do Hashcat gera os candidatos com todas as regras/máscaras, e a ponte despacha os lotes em paralelo para o plugin Python/Rust avaliar o esquema customizado.

## Exemplo
```python
# Estrutura conceitual de funcao de verificacao customizada para esquema proprietario de hash legado
import hashlib

def calc_custom_erp_hash(password: bytes, salt: bytes) -> str:
    inner = hashlib.md5(password).hexdigest().encode("ascii")
    return hashlib.sha256(salt + b":" + inner).hexdigest()
```

## Limites e trade-offs
Para esquemas que combinam apenas duas primitivas padrão (como `md5(sha1($pass))` ou `sha256(md5($pass))`), verifique primeiro na lista `docs/hashcat-example-hashes.md` (`hashcat --example-hashes`) se já existe um modo nativo otimizado em GPU antes de usar a ponte.

## Como verificar
Execute `hashcat --example-hashes | grep -i -B 2 -A 5 "sha256"` para localizar o código `-m` exato de variantes salgadas.

## Conexões
- [[hashcat-hashcat-brain-sessoes-distribuicao-potfile-encrypted-plains]] — Veja também: Hashcat: Operação Avançada — **Hashcat Brain** (`--brain-server` / `--brain-client`), Sessões (`--session` / `--restore`) e **Encrypted Plains**.
- [[hashcat-ataques-pcfg-probabilistic-context-free-grammar-slow-candidates]] — Veja também: Hashcat: Geração Gramatical com **PCFG (*Probabilistic Context-Free Grammar*)** e Modo **`--slow-candidates` (`-S`)**.
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.
- [[hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg]] — Referência cruzada direta com hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
