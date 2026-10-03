---
id: software.seguranca.tranche07.000625
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

# Hashcat: Modos de Hash para Auditoria de Active Directory (`-m 1000` NTLM, `-m 3000` LM, `-m 5600` NetNTLMv2, `-m 13100`/`19700` Kerberoast, `-m 18200` AS-REP e `-m 2100` DCC2)

## Em uma frase
Em uma auditoria completa de segurança de Active Directory (combinada com `impacket-secretsdump`, `GetUserSPNs.py`, `GetNPUsers.py` ou `Responder`), o Hashcat é utilizado para gerar métricas executivas de higiene de senhas do domínio através de seis modos específicos.

## Por que importa
Permite identificar contas com senhas em branco (`aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0`), reutilização de senha entre a conta de usuário comum e a conta `adm_` de Domain Admin (mesmo hash NTLM `-m 1000` sem nem precisar quebrar a senha!) e contas de serviço vulneráveis.

## Como funciona
Os modos essenciais de AD são: **`-m 1000` NTLM** (extraído do `NTDS.dit` ou `SAM`, algoritmo `MD4(UTF-16LE(pass))` sem salt — altíssima velocidade), **`-m 5600` NetNTLMv2** (capturado na rede com Responder), **`-m 13100` Kerberos 5 TGS-REP etype 23** (Kerberoasting RC4), **`-m 19600` / `-m 19700` Kerberos 5 TGS-REP AES128/AES256**, **`-m 18200` Kerberos 5 AS-REP etype 23** (AS-REP Roasting) e **`-m 2100` Domain Cached Credentials 2 (DCC2 / MS Cache v2)** (extraído da colmeia `SECURITY` de estações, PBKDF2-HMAC-SHA1 com 10.240 iterações por padrão).

## Exemplo
```bash
# Auditar hashes de Kerberoasting RC4 (-m 13100) e exibir o relatorio final de contas com senhas fracas (--show)
hashcat -m 13100 -a 0 -O \
  /cases/audit/kerberoast_tgs.txt \
  /opt/secops/wordlists/corp_audit.dict \
  -r /usr/share/hashcat/rules/OneRuleToRuleThemAll.rule

hashcat -m 13100 --show /cases/audit/kerberoast_tgs.txt
```

## Limites e trade-offs
Ao auditar um arquivo `ntds.dit.ntlm` exportado pelo `secretsdump.py` no formato `DOMINIO\usuario:RID:LMHASH:NTHASH:::`, passe a flag **`--username`** ao Hashcat para que ele preserve o nome de usuário associado a cada hash no relatório `--show`.

## Como verificar
Gere estatísticas agregadas (porcentagem de senhas quebradas, comprimento médio, reutilização entre contas Tier 0 e Tier 2) sem jamais expor senhas em texto claro no relatório final.

## Conexões
- [[hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment]] — Veja também: Hashcat: Ataques de Máscara (`-a 3`), *Custom Charsets* (`-1` a `-4`), Arquivos `.hcmask` e Ordenação por **Cadeias de Markov**.
- [[hashcat-hashcat-brain-sessoes-distribuicao-potfile-encrypted-plains]] — Veja também: Hashcat: Operação Avançada — **Hashcat Brain** (`--brain-server` / `--brain-client`), Sessões (`--session` / `--restore`) e **Encrypted Plains**.
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Referência cruzada direta com impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden.
- [[impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa]] — Referência cruzada direta com impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
