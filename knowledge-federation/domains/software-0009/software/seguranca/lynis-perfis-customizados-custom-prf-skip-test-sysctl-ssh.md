---
id: software.seguranca.tranche05.000453
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
fontes: ["https://raw.githubusercontent.com/CISOfy/lynis/master/README.md", "https://cisofy.com/documentation/lynis/get-started/", "https://github.com/CISOfy/lynis-sdk"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CISOfy Lynis: Customização de Políticas com Perfis `custom.prf` (`skip-test`, `config-data` e `--profile`)

## Em uma frase
O Lynis utiliza perfis declarativos (`.prf` localizados em `/etc/lynis/`) onde `default.prf` define os padrões globais e **`custom.prf`** permite adaptar os critérios de auditoria à arquitetura da organização sem modificar `default.prf`.

## Por que importa
Servidores com papéis distintos (ex.: um nó Kubernetes vs um bastião SSH) possuem requisitos diferentes; colocar exceções justificadas (`skip-test`) e valores esperados (`config-data`) em `/etc/lynis/custom.prf` evita que atualizações de pacote sobrescrevam suas regras.

## Como funciona
No `custom.prf`, a diretiva `skip-test=TEST-ID` (ou `skip-test=SSH-7408:loglevel` para pular apenas um subitem específico) silencia falsos positivos documentados, enquanto `config-data=sysctl;kernel.kptr_restrict;2;1;Restrict kernel pointers;` exige que um parâmetro específico do kernel tenha exatamente o valor `2`.

## Exemplo
```ini
# /etc/lynis/custom.prf — Perfil corporativo de hardening Linux
machine-role=server
compliance-standards=cis,iso27001,pcidss

# Exigir endurecimento estrito de ponteiros do kernel e dmesg via sysctl
config-data=sysctl;kernel.kptr_restrict;2;1;Restrict kernel pointers to all users;
config-data=sysctl;kernel.dmesg_restrict;1;1;Restrict dmesg access to privileged users;

# Pular verificação de servidor USB em VMs de nuvem sem barramento USB físico
skip-test=USB-1000
```

## Limites e trade-offs
Nunca edite `/etc/lynis/default.prf` diretamente, pois qualquer atualização do pacote `lynis` via `apt`/`dnf` substituirá o arquivo ou gerará conflito `.dpkg-dist`.

## Como verificar
Execute `sudo lynis show settings` e `sudo lynis show profiles` para confirmar que `/etc/lynis/custom.prf` foi carregado e que as diretivas `skip-test` e `config-data` estão ativas.

## Conexões
- [[lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details]] — Veja também: CISOfy Lynis: Análise de `Warnings` vs `Suggestions`, `/var/log/lynis-report.dat` e `lynis show details <TEST-ID>`.
- [[lynis-hardening-kernel-sysctl-krnl-6000-aslr-ptrace-bpf-rede]] — Veja também: CISOfy Lynis: Remediação de `KRNL-6000` — Hardening de Parâmetros `sysctl` de Kernel, Memória e Pilha de Rede.
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Referência cruzada direta com lynis-arquitetura-auditoria-hardening-unix-linux-test-categories.
- [[lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins]] — Referência cruzada direta com lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
