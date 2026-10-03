---
id: software.devops.tranche04.000385
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

# Depuração detalhada com PACKER_LOG=1 packer build template.pkr.hcl e revisão de chaves sensíveis

## Em uma frase
O guia oficial `.github/CONTRIBUTING.md` do Packer documenta o procedimento canônico para diagnosticar falhas durante a construção de imagens: executar o comando com a variável de ambiente **`PACKER_LOG`** habilitada — por exemplo, **`PACKER_LOG=1 packer build template.pkr.hcl`**. Embora o Packer seja projetado para remover automaticamente chaves sensíveis (strip sensitive keys) da saída de log, a documentação oficial alerta explicitamente para sempre revisar o conteúdo completo do log antes de compartilhá-lo em um Gist ou issue pública por precaução.

## Por que importa
Falhas em builds de imagem frequentemente ocorrem dentro de chamadas de API do provedor de nuvem, negociações SSH/WinRM temporárias ou códigos de retorno de provisionadores remotos que ficam resumidos na saída padrão. O modo `PACKER_LOG=1` expõe toda a comunicação interna e rastros de execução para identificar a causa exata.

## Como funciona
Habilite `PACKER_LOG=1` (e opcionalmente `PACKER_LOG_PATH` para gravar em arquivo) ao investigar timeouts de conexão SSH, erros de permissão IAM no builder ou falhas intermitentes de provisionamento, e revise o arquivo resultante com um scanner de segredos antes de anexá-lo a chamados.

## Exemplo
Quando um build de imagem falha ao aguardar conexão SSH na instância temporária de build, o engenheiro reexecuta com `PACKER_LOG=1 packer build template.pkr.hcl`, identifica no log detalhado que a sub-rede escolhida bloqueava a porta 22 para o runner e corrige o Security Group temporário.

## Limites e trade-offs
Nunca publique a saída bruta de `PACKER_LOG=1` em issues públicas do GitHub ou Gists públicos sem antes inspecionar manualmente se variáveis customizadas de ambiente ou saídas de scripts `echo` imprimiram senhas ou tokens em texto claro.

## Como verificar
Execute `PACKER_LOG=1 packer build` em um template de teste e verifique a emissão detalhada dos logs de diagnóstico e a ocultação de variáveis marcadas como `sensitive`.

## Conexões
- [[packer-local-docker-and-vagrant-box-workflows]] — Veja também: Desenvolvimento e teste local de templates Packer com imagens Docker e Vagrant boxes.
- [[packer-unmaintained-and-archived-plugins-policy]] — Veja também: Política oficial do Packer para plugins comunitários não mantidos e arquivados.

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
