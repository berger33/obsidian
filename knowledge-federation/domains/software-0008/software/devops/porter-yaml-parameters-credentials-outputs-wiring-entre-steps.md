---
id: software.devops.tranche14.001344
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

# Porter: Declaração de Parameters, Credentials e Outputs no porter.yaml

## Em uma frase
O arquivo `porter.yaml` define contratos formais e tipados para **Parameters** (parâmetros de configuração como região, número de réplicas ou domínio), **Credentials** (segredos necessários para autenticar nos provedores, como `kubeconfig` ou chaves de nuvem) e **Outputs** (valores gerados por um passo que alimentam passos seguintes ou são exibidos ao usuário).

## Por que importa
Codificar credenciais ou nomes de ambiente diretamente dentro dos arquivos do instalador impede reutilizar o mesmo bundle imutável em desenvolvimento, homologação e produção.

## Como funciona
No `porter.yaml`, as credenciais declaradas em `credentials:` são mapeadas pelo operador via `porter credentials generate` (injetadas apenas em tempo de execução a partir de variáveis ou cofres de segredos, nunca gravadas na imagem do bundle), enquanto `${bundle.outputs.*}` encadeia a saída do passo Terraform (como a string de conexão do banco) diretamente para os valores do passo Helm.

## Exemplo
```yaml
credentials:
  - name: kubeconfig
    path: /home/nonroot/.kube/config
parameters:
  - name: replicas
    type: integer
    default: 2
```

## Limites e trade-offs
Passar segredos sensíveis (como senhas de banco de dados ou chaves de API) como `parameters` comuns sem `sensitive: true` em vez de `credentials` faz com que os valores apareçam em texto claro no histórico de `porter show`.

## Como verificar
Declare sempre tokens, chaves privadas e `kubeconfig` na seção `credentials:` (ou marque parâmetros secretos como `sensitive: true`).

## Conexões
- [[porter-mixins-helm-terraform-kubernetes-exec-cloud-clis]] — Veja também: Porter: Ecossistema de Mixins (Helm, Terraform, Kubernetes, Docker, AWS, Azure, GCloud e exec).
- [[porter-plugins-secrets-storage-hashicorp-vault-azure-kubernetes]] — Veja também: Porter: Plugins de Armazenamento e Segredos (HashiCorp Vault, Azure Key Vault e Kubernetes).

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
