---
id: software.devops.tranche04.000390
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/packer/main/README.md", "https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md", "https://developer.hashicorp.com/packer/docs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fluxo de infraestrutura imutável combinando Golden Images do Packer com provisionamento IaC

## Em uma frase
A combinação prática apresentada nos guias de AWS e HCP Packer do README oficial separa claramente o ciclo de vida da infraestrutura em duas fases: primeiro, o **Packer** constrói e valida imagens de máquina imutáveis (Golden Images / AMIs) contendo o sistema operacional atualizado, agentes de observabilidade, runtime de contêiner (como CRI-O ou Podman) e configurações de hardening de segurança; segundo, ferramentas de **Infraestrutura como Código** (como Terraform/OpenTofu orquestrados por Terragrunt) provisionam instâncias e grupos de auto-scaling referenciando apenas o ID da imagem pronta.

## Por que importa
Tentar instalar dezenas de pacotes via `cloud-init`/`user-data` no momento em que uma instância sobe em produção torna o auto-scaling lento e sujeito a falhas se um espelho de pacotes externo estiver fora do ar naquele minuto. Com imagens pré-construídas pelo Packer, o boot em produção leva segundos e é 100% determinístico.

## Como funciona
Acione o pipeline do Packer sempre que houver atualização de patch do sistema operacional, versão do Kubernetes/CRI-O ou agentes de segurança, publique a nova imagem após passar por testes automatizados e promova o ID da imagem para o código Terraform/Terragrunt.

## Exemplo
Quando sai uma atualização de segurança do kernel Linux e do CRI-O, o pipeline de imagem gera uma nova AMI com o Packer, executa testes de conformidade em uma instância de homologação e atualiza o Launch Template dos nós Kubernetes via IaC para realizar rolling replacement seguro.

## Limites e trade-offs
Nunca faça login via SSH em instâncias de produção geradas por Golden Images para aplicar mudanças manuais; qualquer alteração deve ser feita no template `.pkr.hcl`, gerando uma nova imagem imutável e substituindo as instâncias.

## Como verificar
Verifique que novas instâncias iniciadas a partir da Golden Image construída pelo Packer entram em estado operacional sem precisar baixar pacotes externos durante o boot.

## Conexões
- [[packer-unified-documentation-and-license-governance]] — Veja também: Repositório unificado de documentação (hashicorp/web-unified-docs) e licença BUSL-1.1 no Packer.

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
