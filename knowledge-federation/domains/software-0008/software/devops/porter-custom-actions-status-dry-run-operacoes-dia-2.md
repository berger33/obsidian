---
id: software.devops.tranche14.001347
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/getporter/porter/main/README.md", "https://porter.sh/docs/quickstart/", "https://github.com/getporter/porter"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Porter: Ações Customizadas de Dia 2 (porter invoke --action) para Diagnóstico, Backup e Dry-Run

## Em uma frase
Além das três ações padrão do ciclo de vida CNAB (`install`, `upgrade` e `uninstall`), o Porter permite declarar **Custom Actions** arbitrárias no `porter.yaml` (como `dry-run`, `status`, `backup`, `restore` ou `rotate-certs`), invocáveis via `porter invoke <instalacao> --action <acao>`.

## Por que importa
Operações recorrentes de Dia 2 (como verificar a saúde de todos os componentes instalados, executar um `terraform plan` de pré-visualização ou disparar um backup consistente antes de uma janela de manutenção) costumam ficar espalhadas em runbooks manuais fora do instalador.

## Como funciona
Declarando uma seção customizada (por exemplo, `status:` ou `backup:`) no `porter.yaml` com seus próprios passos de mixins, o operador executa `porter invoke my-app --action status`, reutilizando exatamente as mesmas credenciais, parâmetros e versões de ferramentas associadas àquela instalação.

## Exemplo
```bash
porter explain --reference ghcr.io/org/cloud-app-installer:v0.2.0 -o json
porter invoke my-app --action status
```

## Limites e trade-offs
Definir uma ação customizada de inspeção (como `status` ou `plan`) que modifica recursos reais sem declarar `modifies: false` no `porter.yaml` faz o Porter tratá-la como uma operação mutável.

## Como verificar
Configure `modifies: false` e `stateless: true` nas ações customizadas que realizam apenas leitura ou diagnóstico no `porter.yaml`.

## Conexões
- [[porter-build-publish-explain-inspecao-contrato-bundle]] — Veja também: Porter: Construção, Publicação OCI e Auto-Documentação de Bundles (build, publish e explain).
- [[porter-archive-air-gapped-thick-bundles-relocacao-imagens]] — Veja também: Porter: Exportação e Relocação de Thick Bundles para Ambientes Air-Gapped (porter archive).

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
