---
id: software.seguranca.tranche15.001430
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

# Pipeline de **Continuous Compliance (Conformidade Contínua)** em CI/CD com OpenSCAP: Validando Golden Images, Parseando `ARF XML` e Prevenindo Drift

## Em uma frase
Como transformar a conformidade regulatória (**PCI-DSS, CIS, STIG, SOC 2**) de um evento manual estressante feito uma vez por ano na véspera da auditoria em um **Pipeline Automatizado de Continuous Compliance** que roda a cada commit de infraestrutura e toda noite na frota de produção?

## Por que importa
Estruturando um pipeline de 3 estágios com o **OpenSCAP**: **(Estágio 1 — Build Time no Packer / Container CI)**: roda `oscap xccdf eval --remediate --tailoring-file tailoring-empresa.xml ...` durante a criação da imagem base e falha o build se restar qualquer regra `high` com `fail`.

## Como funciona
**(Estágio 2— Test Gate)**: valida o `arf.xml` com `xmllint` / `xpath` exigindo `0` falhas não excepcionadas; e **(Estágio 3 — Runtime Drift Detection)**: executa `oscap xccdf eval` semanalmente nos servidores ativos e alerta no SIEM qualquer desvio (*Configuration Drift*)!

## Exemplo
```bash
# Extrair via xmllint/xpath todas as regras com resultado 'fail' de um arquivo ARF XML do OpenSCAP e falhar o job de CI/CD se houver violacoes
FALHAS="$(xmllint --xpath "count(//*[local-name()='rule-result'][*[local-name()='result']='fail'])" ./resultado-auditoria-arf.xml)"
echo "Total de regras XCCDF reprovadas: ${FALHAS}"
test "${FALHAS}" -eq 0
```

## Limites e trade-offs
Por que arquivar os arquivos **`resultado-auditoria-arf.xml`** e **`relatorio-conformidade-cis.html`** gerados pelo OpenSCAP em um bucket S3 com retenção imutável a cada semana economiza centenas de horas durante uma auditoria externa? Porque em vez de tirar prints de tela manuais de dezenas de servidores para o auditor, você entrega o pacote assinado de relatórios **ARF/HTML do OpenSCAP** comprovando historicamente a nota de conformidade de 100% da frota!

## Como verificar
Integre também o OpenSCAP com o **fapolicyd** e o **AIDE** (cujas instalações e regras fazem parte dos próprios perfis CIS Level 2, OSPP e DISA STIG do `scap-security-guide`!).

## Conexões
- [[openscap-kubernetes-compliance-operator-cel-scansettingbinding]] — Veja também: Conformidade de Clusters **Kubernetes e OpenShift** com **ComplianceAsCode (`CEL Content`)** e **Compliance Operator (`ScanSettingBinding`)**.
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Referência cruzada direta com openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
