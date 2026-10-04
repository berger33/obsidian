---
id: software.seguranca.tranche07.000621
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

# Hashcat: Arquitetura de Auditoria de Senhas em GPU (Backends CUDA/HIP/Metal/OpenCL), *In-Kernel Rule Engine* e Perfis de Carga (`-w`)

## Em uma frase
**Hashcat** (`hashcat/hashcat`, licença MIT) é a plataforma open-source de alta performance para auditoria de resistência de senhas e recuperação de hashes em GPUs, CPUs e clusters distribuídos, suportando **mais de 590 algoritmos de hash** (`-m`) e **10 modos de ataque** (`-a`).

## Por que importa
Em auditorias de segurança de Active Directory (`NTDS.dit`, Kerberoasting, NetNTLMv2) ou avaliações de bancos de dados de aplicações, permite comprovar empiricamente quais contas utilizam senhas previsíveis ou se o algoritmo de hash escolhido pela engenharia de software é rápido demais para resistir a GPUs modernas.

## Como funciona
O segredo da velocidade do Hashcat para hashes rápidos (como NTLM `-m 1000`, MD5 `-m 0` ou SHA-256 `-m 1400`) é o seu **In-Kernel Rule Engine**: em vez de a CPU gerar milhões de variações de palavras e sofrer gargalo no barramento PCIe para enviá-las à placa de vídeo, o Hashcat envia a palavra base uma única vez para a GPU e aplica milhares de regras de mutação (`-r`) **diretamente dentro dos núcleos da GPU**.

## Exemplo
```bash
# Identificar dispositivos CUDA/HIP/OpenCL disponiveis (-I) e executar benchmark de algoritmos especificos (-b -m)
hashcat -I
hashcat -b -m 1000 -m 5600 -m 13100 -m 3200
```

## Limites e trade-offs
A flag **`-w <1..4>` (`--workload-profile`)** controla o consumo de recursos e a responsividade térmica (`1` = Low, `2` = Default, `3` = High para servidores dedicados de auditoria, `4` = Nightmare), enquanto **`-O` (`--optimized-kernel-enable`)** ativa kernels otimizados com throughput superior (limitando o comprimento máximo da senha candidata, ex.: 31 caracteres na maioria dos modos rápidos).

## Como verificar
Compare na saída de `hashcat -b` a diferença de bilhões de hashes/segundo do NTLM (`-m 1000`) contra dezenas de milhares de hashes/segundo do `bcrypt` (`-m 3200`) ou `Argon2`.

## Conexões
- [[hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg]] — Veja também: Hashcat: Os Modos de Ataque (`-a 0` Wordlist, `-a 1` Combinator, `-a 3` Mask/Brute-Force, `-a 6`/`-a 7` Hybrid e `-a 9` Association).
- [[hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras]] — Referência cruzada direta com hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras.
- [[responder-auditoria-offline-senhas-hashcat-netntlmv2-netntlmv1-regras]] — Referência cruzada direta com responder-auditoria-offline-senhas-hashcat-netntlmv2-netntlmv1-regras.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
