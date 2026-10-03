---
id: software.devops.tranche04.000386
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

# Política oficial do Packer para plugins comunitários não mantidos e arquivados

## Em uma frase
O README oficial do Packer esclarece o que acontece quando a manutenção de um plugin comunitário desacelera e a HashiCorp utiliza a opção de arquivamento do GitHub para sinalizar claramente seu status como **unmaintained (não mantido)**: (1) o repositório de código e todo o histórico de commits continuam disponíveis; (2) a documentação permanece publicada no site do Packer; (3) issues e pull requests são monitorados apenas em regime de melhor esforço (best effort); e (4) **nenhum desenvolvimento ativo será realizado pela HashiCorp** naquele plugin (embora interessados possam contatar `packer@hashicorp.com` para assumir a manutenção).

## Por que importa
Continuar dependendo de um plugin arquivado/não mantido em pipelines críticos de produção cria risco de obsolescência quando o provedor de nuvem ou hipervisor subjacente descontinuar versões antigas de API ou quando surgirem CVEs em dependências do plugin.

## Como funciona
Audite periodicamente os blocos `required_plugins` de todos os templates `.pkr.hcl` da organização contra o catálogo `developer.hashicorp.com/packer/integrations` e os repositórios GitHub correspondentes para verificar se algum plugin utilizado foi arquivado.

## Exemplo
Durante uma revisão anual da cadeia de suprimentos de infraestrutura, a equipe verifica o status dos plugins declarados nos templates Packer e substitui um post-processor comunitário arquivado por uma integração ativamente mantida.

## Limites e trade-offs
Não confunda a presença contínua da documentação de um plugin no site do Packer com garantia de suporte ativo: conforme a política oficial, a documentação de plugins arquivados é mantida online para referência histórica mesmo sem desenvolvimento ativo.

## Como verificar
Verifique no GitHub e na página do plugin em `developer.hashicorp.com/packer/integrations` que todas as integrações utilizadas nos seus builds estão em repositórios ativos e não arquivados.

## Conexões
- [[packer-packer-log-debugging-and-secret-sanitization]] — Veja também: Depuração detalhada com PACKER_LOG=1 packer build template.pkr.hcl e revisão de chaves sensíveis.
- [[packer-hcl2-templates-and-reproducible-test-cases]] — Veja também: Templates HCL2 (template.pkr.hcl) e criação de casos de teste mínimos reproduzíveis no Packer.

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
