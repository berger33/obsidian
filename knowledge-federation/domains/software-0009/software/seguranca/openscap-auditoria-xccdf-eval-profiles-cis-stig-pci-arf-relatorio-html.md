---
id: software.seguranca.tranche15.001422
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

# Executando Auditorias de Conformidade com **`oscap xccdf eval`**: Perfis **CIS Level 1/2, DISA STIG, PCI-DSS e OSPP**, Resultados **`--results-arf`** e Relatórios HTML

## Em uma frase
Como executar uma varredura completa de conformidade **CIS Server Level 2** ou **DISA STIG** em um servidor Linux usando o **`oscap xccdf eval`** e gerar simultaneamente: **(1) Um relatório visual interativo em HTML (`--report`)** para os auditores e gestores e **(2) Um arquivo estruturado `ARF` (`--results-arf`)** para ingestão automatizada no SIEM/ Satélite/Foreman?

## Por que importa
Com uma única execução do subcomando **`oscap xccdf eval`**!

## Como funciona
Ao passar **`--profile <id_do_perfil>`** (ou apenas o sufixo curto do perfil, ex.: `--profile cis` ou `--profile stig` nas versões modernas do `oscap`!), o motor OpenSCAP executa em segundos centenas de sondas **OVAL** em modo somente-leitura (verificando parâmetros de kernel `sysctl`, opções de montagem `/etc/fstab`, algoritmos do `sshd_config`, regras `auditd`, `pam_faillock`, `sudoers`, `nftables` e permissões SUID) e imprime no terminal o resultado de cada regra (`pass`, `fail`, `notapplicable`, `notchecked`)!

## Exemplo
```bash
# Executar auditoria XCCDF com o perfil CIS Server Level 2 gerando relatorio visual HTML e arquivo de resultados ARF XML
oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis \
  --results-arf ./resultado-auditoria-arf.xml \
  --report ./relatorio-conformidade-cis.html \
  /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
```

## Limites e trade-offs
Atenção ao código de saída (*Exit Code*) do comando **`oscap xccdf eval`** quando você o coloca dentro de um pipeline de CI/CD ou script Bash: **`0`** significa que 100% das regras aplicáveis passaram (`pass`); **`1`** significa erro fatal de execução; e **`2`** significa que a auditoria rodou com sucesso, mas **pelo menos uma regra de conformidade falhou (`fail`)**!

## Como verificar
Se você também quiser gerar um guia de implementação legível por humanos (em HTML) descrevendo cada controle do perfil antes mesmo de escanear uma máquina, basta rodar **`oscap xccdf generate guide --profile cis /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml > guia-cis.html`**!

## Conexões
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Veja também: Arquitetura do **OpenSCAP (`OpenSCAP/openscap`)** e **ComplianceAsCode (`scap-security-guide`)**: Padrões NIST SCAP (`XCCDF`, `OVAL`, `CPE`, `ARF`) e CLI **`oscap`**.
- [[openscap-remediacao-automatizada-online-remediate-ansible-bash-playbooks]] — Veja também: Remediação Automatizada de Hardening no OpenSCAP: Exportando **Playbooks Ansible (`--fix-type ansible`)**, Scripts **Bash (`--fix-type bash`)** vs. `--remediate`.
- [[openscap-customizacao-perfis-tailoring-files-variaveis-excecoes-xccdf]] — Referência cruzada direta com openscap-customizacao-perfis-tailoring-files-variaveis-excecoes-xccdf.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
