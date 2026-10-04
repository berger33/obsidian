---
id: software.seguranca.tranche05.000489
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://gitlab.com/apparmor/apparmor/-/raw/master/README.md", "https://gitlab.com/apparmor/apparmor/-/wikis/home", "https://gitlab.com/apparmor/apparmor/-/wikis/Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AppArmor: Diagnóstico de Negativas (`apparmor="DENIED"`), `aa-notify` e Decodificação de Campos `operation`, `requested_mask` e `denied_mask`

## Em uma frase
Quando o módulo AppArmor do kernel bloqueia uma ação em modo `enforce` (ou registra em modo `complain`), ele emite um evento LSM (`type=AVC` / `apparmor="DENIED"` ou `apparmor="ALLOWED"`) para o subsistema `auditd` (ou `dmesg`/`journald` caso o `auditd` não esteja rodando).

## Por que importa
Compreender os campos exatos do log de negação (`profile`, `operation`, `name`, `pid`, `comm`, `requested_mask`, `denied_mask` e `fsuid`/`ouid`) permite distinguir imediatamente um erro legítimo de configuração de perfil de uma tentativa real de exploração pós-comprometimento.

## Como funciona
Por exemplo, um evento com `apparmor="DENIED" operation="open" profile="myapp" name="/etc/myapp/db.conf" requested_mask="r" denied_mask="r" fsuid=1001 ouid=0` indica que o processo `myapp` (rodando como UID `1001`) tentou ler `/etc/myapp/db.conf` (cujo dono é `root`, `ouid=0`): se a regra no perfil tiver o prefixo `owner /etc/myapp/** r,`, a negação ocorreu porque `fsuid (1001) != ouid (0)`.

## Exemplo
```bash
# Filtrar todas as violacoes do AppArmor registradas hoje no auditd ou journald do kernel
sudo ausearch -m AVC -ts today | grep 'apparmor="DENIED"'
sudo journalctl -k --since today | grep 'apparmor="DENIED"'
```

## Limites e trade-offs
Quando um acesso falha silenciosamente sem aparecer nos logs com `apparmor="DENIED"`, verifique se o perfil possui uma regra explícita **`deny`** (que suprime o log por padrão); remova temporariamente o `deny` ou troque por `audit deny` durante a depuração.

## Como verificar
Compare `fsuid` e `ouid` e a máscara `denied_mask` no log do kernel para ajustar cirurgicamente o perfil afetado.

## Conexões
- [[apparmor-subperfis-change-hat-pam-apparmor-mod-apparmor]] — Veja também: AppArmor: Mudança Dinâmica de Privilégio Intra-Processo com `aa_change_hat(2)`, `aa_change_profile(2)` e `pam_apparmor`.
- [[apparmor-otimizacao-cache-binario-apparmor-parser-boot-systemd]] — Veja também: AppArmor: Compilação AOT, Cache Binário (`/var/cache/apparmor/`), Pré-Validação em CI e Hardening de Boot (`apparmor=1 security=apparmor`).
- [[apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce]] — Referência cruzada direta com apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce.
- [[apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd]] — Referência cruzada direta com apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Referência cruzada direta com auditd-investigacao-forense-ausearch-aureport-auid-correlacao.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
