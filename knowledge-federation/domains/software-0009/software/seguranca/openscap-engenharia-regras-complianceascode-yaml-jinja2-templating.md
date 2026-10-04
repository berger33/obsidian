---
id: software.seguranca.tranche15.001428
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

# Como Escrever Regras Customizadas no **`ComplianceAsCode/content`**: `rule.yml`, Templates Parametrizados Jinja2 e Compilação Multi-Formato (`XCCDF`, `OVAL`, `Ansible`, `Bash`, `CEL`)

## Em uma frase
Como o projeto **`ComplianceAsCode/content`** consegue manter milhares de regras de segurança sincronizadas para dezenas de distribuições Linux gerando simultaneamente **SCAP (`XCCDF` + `OVAL`)**, **Playbooks Ansible**, **Scripts Bash** e **Regras Kubernetes (`CEL`)** sem duplicar código?

## Por que importa
Conforme detalhado no `README.md` do `ComplianceAsCode/content`, através de uma arquitetura **"Write Once in YAML + Templates Jinja2"**: cada regra vive em seu próprio diretório contendo um arquivo declarativo **`rule.yml`** (com `title`, `description`, `rationale`, `severity`, `identifiers: cce/stigid` e `references: cis/nist/pcidss`)!

## Como funciona
Em vez de escrever manualmente 50 linhas de XML OVAL, 20 linhas de Ansible e 15 linhas de Bash para verificar/configurar uma opção do `sshd_config`, uma permissão de arquivo ou um parâmetro `sysctl`, basta declarar no final do `rule.yml` um **`template:` padronizado** (ex.: `template: name: sshd_lineinfile`, `sysctl`, `package_installed`, `service_enabled`, `file_permissions`) — e o sistema de build (`./build_product`) compila automaticamente o XML OVAL, a task Ansible e o fix Bash para cada distribuição!

## Exemplo
```yaml
# Exemplo de definicao declarativa rule.yml no ComplianceAsCode usando template parametrizado para gerar OVAL + Ansible + Bash automaticamente
documentation_complete: true
title: 'Disable SSH Root Login'
description: |-
    Root login via SSH should be disabled by setting <tt>PermitRootLogin no</tt> in <tt>/etc/ssh/sshd_config</tt>.
rationale: |-
    Disabling direct root login forces administrators to authenticate with their individual accounts before escalating privileges.
severity: high
identifiers:
    cce@rhel9: CCE-83450-7
references:
    cis@rhel9: 5.2.10
    nist: IA-2(1)
template:
    name: sshd_lineinfile
    vars:
        parameter: PermitRootLogin
        value: 'no'
```

## Limites e trade-offs
Olhe as 5 últimas linhas (`template: name: sshd_lineinfile`) do `rule.yml` acima: com apenas 5 linhas de configuração de template, o compilador do `ComplianceAsCode` gera sozinho a sonda OVAL que inspeciona `/etc/ssh/sshd_config` e `/etc/ssh/sshd_config.d/*.conf`, a task Ansible `lineinfile` e o script Bash de remediação!

## Como verificar
Para compilar apenas uma regra específica ou uma distribuição durante o desenvolvimento local no repositório `ComplianceAsCode/content`, execute **`./build_product rhel9`** (ou `./build_product ubuntu2404`).

## Conexões
- [[openscap-auditoria-remota-oscap-ssh-automacao-agentless-bastion]] — Veja também: Varredura Remota Agentless via SSH com **`oscap-ssh`**: Auditando e Remediando Frotas de Servidores Linux sem Instalar Agentes Permanentes.
- [[openscap-kubernetes-compliance-operator-cel-scansettingbinding]] — Veja também: Conformidade de Clusters **Kubernetes e OpenShift** com **ComplianceAsCode (`CEL Content`)** e **Compliance Operator (`ScanSettingBinding`)**.
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.
- [[openscap-customizacao-perfis-tailoring-files-variaveis-excecoes-xccdf]] — Referência cruzada direta com openscap-customizacao-perfis-tailoring-files-variaveis-excecoes-xccdf.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
