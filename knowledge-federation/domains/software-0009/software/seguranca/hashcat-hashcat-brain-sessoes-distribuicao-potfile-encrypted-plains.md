---
id: software.seguranca.tranche07.000626
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

# Hashcat: Operação Avançada — **Hashcat Brain** (`--brain-server` / `--brain-client`), Sessões (`--session` / `--restore`) e **Encrypted Plains**

## Em uma frase
Conforme documentado no `README.md` oficial e em `docs/hashcat-brain.md`, o **Hashcat Brain** é um servidor em memória de deduplicação inteligente de candidatos (`--brain-server` / `--brain-client`) que registra hashes curtos (xxHash64) das senhas candidatas e ataques já testados em sessões anteriores.

## Por que importa
Em auditorias recorrentes ou quando múltiplas listas de palavras e regras sobrepostas são executadas, até 60% dos candidatos gerados já foram testados antes contra aquela mesma lista de hashes; o *Hashcat Brain* pula instantaneamente qualquer candidato já avaliado no passado.

## Como funciona
Adicionalmente, para conformidade rigorosa de privacidade onde o auditor precisa provar quais contas têm senhas fracas **sem poder ler a senha do usuário em texto claro**, o recurso **Encrypted Plains** (`docs/hashcat-encrypted-plains.md`) permite cifrar o dicionário/candidatos com a chave pública do proprietário do sistema.

## Exemplo
```bash
# Iniciar uma sessao nomeada persistente (--session) que pode ser pausada e retomada a qualquer momento (--restore)
hashcat --session audit_ad_q4 -m 1000 -a 0 \
  --potfile-path /cases/audit/q4_audit.pot \
  /cases/audit/ntds_hashes.txt \
  /opt/secops/wordlists/corp_audit.dict \
  -r /usr/share/hashcat/rules/best64.rule

# Retomar a sessao exatamente do ponto de interrupcao
hashcat --session audit_ad_q4 --restore
```

## Limites e trade-offs
Sempre isole cada cliente ou auditoria usando **`--potfile-path /cases/cliente_x/audit.pot`** (ou `--potfile-disable`): usar o `hashcat.potfile` global padrão mistura hashes quebrados de auditorias diferentes na mesma máquina.

## Como verificar
Verifique que o diretório `/cases/audit/` com o arquivo `.pot` e `.restore` está armazenado em volume criptografado LUKS e é destruído de forma segura (`shred -u`) ao término do contrato de auditoria.

## Conexões
- [[hashcat-auditoria-active-directory-ntds-kerberoasting-asrep-dcc2]] — Veja também: Hashcat: Modos de Hash para Auditoria de Active Directory (`-m 1000` NTLM, `-m 3000` LM, `-m 5600` NetNTLMv2, `-m 13100`/`19700` Kerberoast, `-m 18200` AS-REP e `-m 2100` DCC2).
- [[hashcat-extensibilidade-assimilation-bridge-plugins-python-rust-c]] — Veja também: Hashcat v7+: **Assimilation Bridge** para Criação de Novos Modos de Hash em **Python, Rust ou C** sem Escrever Kernels GPU.
- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Referência cruzada direta com hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules.

## Fontes
- [Hashcat Official GitHub — Architecture, Attack Modes & Features](https://raw.githubusercontent.com/hashcat/hashcat/master/README.md) — documentação oficial do Hashcat cobrindo backends CUDA/HIP/Metal/OpenCL, In-Kernel Rule Engine, Assimilation Bridge, Brain e Encrypted Plains; consultado em 2026-10-03.
- [Hashcat Official Wiki — Rule-Based Attack Reference](https://hashcat.net/wiki/doku.php?id=rule_based_attack) — referência oficial da linguagem de regras de mutação in-kernel, multi-rules e depuração de regras do Hashcat; consultado em 2026-10-03.
- [Hashcat Official Wiki — Mask Attack & Custom Charsets](https://hashcat.net/wiki/doku.php?id=mask_attack) — documentação oficial de ataques de máscara, charsets customizados e cadeias de Markov no Hashcat; consultado em 2026-10-03.
