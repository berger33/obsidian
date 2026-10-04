---
id: software.seguranca.tranche05.000486
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

# AppArmor: Criação e Refinamento Guiado de Perfis com `aa-genprof`, `aa-logprof` e `aa-autodep`

## Em uma frase
O pacote `apparmor-utils` fornece ferramentas interativas baseadas em aprendizado dinâmico — **`aa-autodep`**, **`aa-genprof`** e **`aa-logprof`** — que analisam os eventos de auditoria do kernel (`/var/log/audit/audit.log` ou `/var/log/syslog`) e propõem regras e abstrações adequadas.

## Por que importa
Em aplicações complexas que carregam dezenas de bibliotecas dinâmicas e arquivos de localização no startup, usar `aa-genprof` reduz de dias para minutos o tempo necessário para construir um perfil funcional.

## Como funciona
O comando `sudo aa-genprof /usr/local/bin/myapp` gera um esqueleto mínimo em modo `complain`, instrui o engenheiro a exercitar as funcionalidades da aplicação em outro terminal e, ao pressionar `S` (*Scan*), lê todas as solicitações registradas no `auditd`, sugerindo se o analista deseja permitir o caminho exato, usar um glob, incluir uma `abstraction` correspondente ou negar (`Deny`). Posteriormente, **`sudo aa-logprof`** refina perfis existentes a partir de novos logs.

## Exemplo
```bash
# Analisar logs recentes do auditd para refinar perfis em modo complain ou investigar negacoes
sudo aa-logprof -f /var/log/audit/audit.log
```

## Limites e trade-offs
Nunca aprove cegamente (`Allow`) todas as sugestões do `aa-logprof` em um servidor que já esteja exposto a tráfego externo não confiável, pois você poderia incorporar o comportamento de uma tentativa de ataque dentro do perfil permitido; execute `aa-genprof` apenas em ambiente controlado de homologação/CI.

## Como verificar
Após revisar o perfil gerado pelo `aa-genprof` em Git, execute `sudo apparmor_parser -r` e confirme zero mensagens `apparmor="DENIED"` sob carga normal.

## Conexões
- [[apparmor-abstracoes-tunables-local-overrides-manutencao-perfis]] — Veja também: AppArmor: Modularização com `abstractions/`, Variáveis `tunables/` e Customizações Seguras em `local/`.
- [[apparmor-integracao-containers-docker-kubernetes-securitycontext]] — Veja também: AppArmor: Confinamento de Containers e Pods Kubernetes (`securityContext.appArmorProfile` GA no Kubernetes v1.30+).
- [[apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce]] — Referência cruzada direta com apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce.
- [[apparmor-diagnostico-violacoes-apparmor-denied-dmesg-ausearch]] — Referência cruzada direta com apparmor-diagnostico-violacoes-apparmor-denied-dmesg-ausearch.
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Referência cruzada direta com auditd-investigacao-forense-ausearch-aureport-auid-correlacao.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
