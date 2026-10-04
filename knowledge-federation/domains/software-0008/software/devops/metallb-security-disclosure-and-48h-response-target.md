---
id: software.devops.tranche05.000450
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/metallb/metallb/main/README.md", "https://metallb.io/concepts/", "https://github.com/metallb/metallb"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Reporte de vulnerabilidades de segurança e meta de resposta inicial em 48 horas no MetalLB

## Em uma frase
A seção *Reporting security issues* do README oficial do MetalLB documenta o processo de divulgação de segurança do projeto: problemas de segurança podem ser reportados no issue tracker do GitHub ou, caso o relator prefira **divulgação privada (private disclosure)**, enviados por e-mail diretamente a todos os mantenedores listados no README (`fpaoline@redhat.com` e `obraunsh@redhat.com`). Os mantenedores estabelecem a meta de fornecer **resposta inicial aos relatos de vulnerabilidade dentro de 48 horas**, variando o prazo de correção conforme a complexidade do problema.

## Por que importa
Por executar o DaemonSet `speaker` com acesso direto à pilha de rede do nó host (`hostNetwork`) e manipular pacotes ARP, NDP e sessões BGP com roteadores físicos do data center, vulnerabilidades no processamento de pacotes de rede ou na validação de webhooks do MetalLB exigem tratamento cuidadoso e canal privado.

## Como funciona
Caso identifique uma vulnerabilidade explorável no MetalLB durante auditorias de segurança de rede, utilize preferencialmente o canal de divulgação privada por e-mail aos mantenedores para permitir a elaboração do patch antes da exposição pública.

## Exemplo
Um pesquisador de segurança identifica uma condição de falha no parser de configuração BGP e envia os detalhes técnicos por e-mail privado aos mantenedores listados no README, recebendo confirmação dentro da janela de 48 horas.

## Limites e trade-offs
Acompanhe as notas de versão do MetalLB e os avisos de segurança dos pacotes subjacentes (como o FRRouting quando utilizado no modo BGP FRR) para manter os pods `speaker` e `controller` atualizados contra CVEs de rede.

## Como verificar
Confirme no inventário de governança do cluster a versão instalada do MetalLB e os canais oficiais de suporte e segurança documentados no repositório `metallb/metallb`.

## Conexões
- [[metallb-stable-release-branches-versus-main-branch-deployments]] — Veja também: Governança de implantação do MetalLB: uso obrigatório de releases estáveis em vez da branch main.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
