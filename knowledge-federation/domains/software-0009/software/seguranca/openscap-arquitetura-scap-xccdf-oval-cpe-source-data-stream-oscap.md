---
id: software.seguranca.tranche15.001421
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md", "https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **OpenSCAP (`OpenSCAP/openscap`)** e **ComplianceAsCode (`scap-security-guide`)**: Padrões NIST SCAP (`XCCDF`, `OVAL`, `CPE`, `ARF`) e CLI **`oscap`**

## Em uma frase
Como governos, bancos, hospitais e operadores de infraestrutura crítica auditam e comprovam automaticamente que milhares de servidores Linux (**RHEL, Fedora, Ubuntu, Debian, SUSE, AlmaLinux, Rocky Linux**) estão em conformidade com benchmarks rigorosos como **CIS Benchmarks, DISA STIG, PCI-DSS, ANSSI, HIPAA e ISO 27001**?

## Por que importa
Através da dupla open-source certificada pelo NIST: **(1) O motor de linha de comando `oscap` (`OpenSCAP`)** e **(2) O repositório de políticas `ComplianceAsCode/content` (distribuído nas distros como o pacote `scap-security-guide` / `ssg-*`)**!

## Como funciona
Juntos, eles implementam o padrão **SCAP (*Security Content Automation Protocol*)** empacotado em um único arquivo **SCAP Source Data Stream (`*-ds.xml`)** que reúne: **(A) `XCCDF` (*Extensible Configuration Checklist Description Format*)** — define os Perfis (`Profiles`), Regras, Severidades e Scripts de Remediação; **(B) `OVAL` (*Open Vulnerability and Assessment Language*)** — as sondas declarativas que inspecionam arquivos, pacotes, sysctl, systemd e permissões no sistema operacional; **(C) `CPE` (*Common Platform Enumeration*)** — identifica o sistema alvo; e **(D) `ARF` (*Asset Reporting Format*)**!

## Exemplo
```bash
# Inspecionar todos os perfis de conformidade (CIS, STIG, PCI-DSS, ANSSI, OSPP) disponiveis em um SCAP Data Stream com oscap info
oscap --version
oscap info /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
oscap ds sds-validate /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
```

## Limites e trade-offs
Veja os dois comandos iniciais fundamentais acima: **`oscap info <arquivo-ds.xml>`** lista o ID exato de todos os **Profiles** contidos naquele Data Stream (ex.: `xccdf_org.ssgproject.content_profile_cis`, `..._stig`, `..._pci-dss`, `..._anssi_bp28_high`), e **`oscap ds sds-validate`** valida criptográfica e estruturalmente o schema XML de todos os componentes (`XCCDF`, `OVAL`, `OCIL`, `CPE`) antes da execução!

## Como verificar
No Debian/Ubuntu, instale os Data Streams oficiais com `apt install openscap-scanner ssg-debian ssg-debderived`; no RHEL/Fedora/Alma/Rocky, instale com `dnf install openscap-scanner scap-security-guide`.

## Conexões
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Veja também: Executando Auditorias de Conformidade com **`oscap xccdf eval`**: Perfis **CIS Level 1/2, DISA STIG, PCI-DSS e OSPP**, Resultados **`--results-arf`** e Relatórios HTML.
- [[openscap-remediacao-automatizada-online-remediate-ansible-bash-playbooks]] — Referência cruzada direta com openscap-remediacao-automatizada-online-remediate-ansible-bash-playbooks.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
