---
id: software.seguranca.tranche15.001424
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

# Customização de Benchmarks Corporativos no OpenSCAP com **Tailoring Files (`--tailoring-file`)**: Ajustando Variáveis XCCDF e Desabilitando Regras Incompatíveis

## Em uma frase
Todo engenheiro de segurança já viveu este dilema: o benchmark **CIS Level 2** ou **DISA STIG** oficial traz 300 regras excelentes, mas 3 regras específicas (por exemplo, um timeout de SSH curto demais para uma aplicação legada ou uma partição `/var/tmp` separada que não existe nas VMs da nuvem) quebram o seu ambiente. Se você editar o arquivo `/usr/share/xml/scap/ssg/content/ssg-*-ds.xml` diretamente, **a próxima atualização do pacote `scap-security-guide` sobrescreverá suas edições**!

## Por que importa
Qual é a maneira padrão SCAP de customizar um perfil oficial sem nunca tocar no Data Stream original?

## Como funciona
Usando um **XCCDF Tailoring File (`--tailoring-file custom-tailoring.xml`)**, gerado visualmente no **SCAP Workbench** ou via linha de comando **`autotailor`**! Um **Tailoring File** é um pequeno arquivo XML versionado no Git da sua empresa que cria um perfil derivado (`xccdf_empresa_profile_cis_custom`) sobre o Data Stream oficial realizando três operações limpas: **(1) Desmarcar regras com exceção de risco aprovada (`<xccdf:select idref="..." selected="false"/>`)**, **(2) Incluir regras extras de outros perfis (`selected="true"`)** e **(3) Alterar o valor de variáveis parametrizadas (`<xccdf:set-value idref="var_sshd_idle_timeout_value">600</xccdf:set-value>`)**!

## Exemplo
```bash
# Criar um Tailoring File customizado via CLI (autotailor) ajustando uma variavel XCCDF e desabilitando uma regra especifica com excecao documentada
autotailor \
  --output ./tailoring-empresa-cis.xml \
  --new-profile-id cis_empresa_custom \
  --var-value var_accounts_tmout=900 \
  --unselect grub2_password \
  /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml cis
oscap xccdf eval --tailoring-file ./tailoring-empresa-cis.xml --profile cis_empresa_custom /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
```

## Limites e trade-offs
Veja que elegância técnica no utilitário **`autotailor`** acima: em uma única linha de comando você deriva o perfil `cis_empresa_custom`, altera a variável `var_accounts_tmout=900` (15 minutos) e desmarca a regra `grub2_password` (ex.: para VMs em nuvem sem console físico), mantendo 100% de compatibilidade com futuras atualizações do pacote `scap-security-guide`!

## Como verificar
Em auditorias formais (PCI-DSS / ISO 27001), versionar o arquivo `tailoring-empresa-cis.xml` no Git com a justificativa de cada `--unselect` no commit permite que o auditor veja imediatamente todas as exceções corporativas em menos de 30 linhas de XML!

## Conexões
- [[openscap-remediacao-automatizada-online-remediate-ansible-bash-playbooks]] — Veja também: Remediação Automatizada de Hardening no OpenSCAP: Exportando **Playbooks Ansible (`--fix-type ansible`)**, Scripts **Bash (`--fix-type bash`)** vs. `--remediate`.
- [[openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds]] — Veja também: Varredura de Vulnerabilidades de Pacotes (**CVE Scanning**) com **`oscap oval eval`**: Avaliando Feeds OVAL Oficiais (Red Hat, Ubuntu, Debian, SUSE, AlmaLinux).
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Referência cruzada direta com openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html.
- [[openscap-engenharia-regras-complianceascode-yaml-jinja2-templating]] — Referência cruzada direta com openscap-engenharia-regras-complianceascode-yaml-jinja2-templating.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
