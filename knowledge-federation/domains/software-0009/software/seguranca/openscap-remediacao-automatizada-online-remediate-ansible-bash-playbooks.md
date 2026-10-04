---
id: software.seguranca.tranche15.001423
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

# Remediação Automatizada de Hardening no OpenSCAP: Exportando **Playbooks Ansible (`--fix-type ansible`)**, Scripts **Bash (`--fix-type bash`)** vs. `--remediate`

## Em uma frase
Depois que o `oscap xccdf eval` aponta 45 falhas de configuração em relação ao benchmark **CIS** ou **DISA STIG**, corrigir 45 arquivos de configuração manualmente em centenas de servidores levaria semanas. Como o **OpenSCAP + ComplianceAsCode** automatiza a correção (**Remediação**) dessas falhas de forma segura e auditável via **GitOps / Ansible**?

## Por que importa
O OpenSCAP oferece **dois caminhos de remediação**: **(Caminho 1 — Recomendado para Produção: Geração de Playbook Ansible ou Script Bash via `oscap xccdf generate fix`)** e **(Caminho 2 — Remediação Inline: `oscap xccdf eval --remediate`)**!

## Como funciona
Com **`oscap xccdf generate fix --fix-type ansible --profile cis ...`**, o OpenSCAP extrai do Data Stream um **Playbook Ansible completo e idempotente** (ou, se você passar `--result-id` sobre um arquivo `arf.xml` de um scan recém-feito, ele gera um Playbook Ansible contendo **apenas as correções para as regras específicas que falharam naquela máquina**!)!

## Exemplo
```bash
# Gerar um Playbook Ansible idempotente contendo apenas as correcoes para as regras que falharam no arquivo resultado-auditoria-arf.xml
oscap xccdf generate fix \
  --fix-type ansible \
  --result-id "" \
  --output ./remediacao-falhas-cis.yml \
  ./resultado-auditoria-arf.xml
ansible-playbook ./remediacao-falhas-cis.yml --check --diff
```

## Limites e trade-offs
Olhe a segurança operacional do fluxo **`oscap xccdf generate fix --fix-type ansible`** combinado com **`ansible-playbook --check --diff`** acima: em vez de aplicar alterações às cegas diretamente em produção com `--remediate`, você gera o playbook YAML, simula com `--check --diff` para ver cada linha de `/etc/ssh/sshd_config` ou `/etc/sysctl.d/` que será modificada, submete a Pull Request para revisão da equipe e aplica com segurança!

## Como verificar
Para a construção de **Golden Images (Packer / Kickstart / Image Builder)** em pipelines de CI/CD onde a máquina ainda não está em produção, usar diretamente `oscap xccdf eval --remediate --profile cis ...` já entrega a imagem da VM 100% endurecida de fábrica!

## Conexões
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Veja também: Executando Auditorias de Conformidade com **`oscap xccdf eval`**: Perfis **CIS Level 1/2, DISA STIG, PCI-DSS e OSPP**, Resultados **`--results-arf`** e Relatórios HTML.
- [[openscap-customizacao-perfis-tailoring-files-variaveis-excecoes-xccdf]] — Veja também: Customização de Benchmarks Corporativos no OpenSCAP com **Tailoring Files (`--tailoring-file`)**: Ajustando Variáveis XCCDF e Desabilitando Regras Incompatíveis.
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
