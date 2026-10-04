---
id: software.seguranca.tranche15.001429
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

# Conformidade de Clusters **Kubernetes e OpenShift** com **ComplianceAsCode (`CEL Content`)** e **Compliance Operator (`ScanSettingBinding`)**

## Em uma frase
Como auditar continuamente um cluster **Kubernetes / OpenShift** contra os benchmarks **CIS Kubernetes Benchmark** e **NSA/CISA Kubernetes Hardening Guide** usando o ecossistema **OpenSCAP + ComplianceAsCode**, sem precisar abrir sessões SSH manuais nos Worker Nodes?

## Por que importa
Conforme documentado no `ComplianceAsCode/content`, através do **Compliance Operator** combinado com dois formatos nativos: **(1) SCAP Data Streams para os Nodes e para a API do Cluster** (executados em Pods coletores gerenciados pelo operador e persistidos em `ComplianceCheckResult` CRDs) e **(2) O novo formato `CEL Content` (*Common Expression Language*)**!

## Como funciona
O **CEL Content** do ComplianceAsCode compila as regras de segurança diretamente em expressões **CEL em YAML** que avaliam os recursos nativos da API do Kubernetes (como `PodSecurity`, `NetworkPolicy`, `RBAC`, `APIServer`, `KubeletConfig`) sem exigir acesso de shell nos nós!

## Exemplo
```bash
# Inspecionar no cluster Kubernetes/OpenShift os perfis de conformidade carregados pelo Compliance Operator e os resultados por regra
kubectl get profiles.compliance -n openshift-compliance
kubectl get compliancesuites -n openshift-compliance
kubectl get compliancecheckresults -n openshift-compliance -l compliance.openshift.io/check-status=FAIL
```

## Limites e trade-offs
Quando o **Compliance Operator** detecta que uma regra do CIS Benchmark falhou (`status: FAIL`), ele também cria um objeto **`ComplianceRemediation`** correspondente: se o administrador aprovar a remediação (`spec.apply: true`), o próprio operador aplica o manifesto de correção no cluster de forma declarativa!

## Como verificar
Combine o **Compliance Operator / CEL Content** com o **Kyverno** para garantir tanto auditoria periódica de conformidade do cluster quanto bloqueio preventivo no Admission Controller.

## Conexões
- [[openscap-engenharia-regras-complianceascode-yaml-jinja2-templating]] — Veja também: Como Escrever Regras Customizadas no **`ComplianceAsCode/content`**: `rule.yml`, Templates Parametrizados Jinja2 e Compilação Multi-Formato (`XCCDF`, `OVAL`, `Ansible`, `Bash`, `CEL`).
- [[openscap-integracao-ci-cd-oscap-arf-to-json-autotailor-governanca]] — Veja também: Pipeline de **Continuous Compliance (Conformidade Contínua)** em CI/CD com OpenSCAP: Validando Golden Images, Parseando `ARF XML` e Prevenindo Drift.
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
