---
id: software.kubernetes.networkpolicy-isolamento.000001
tipo: tecnica
dominio: software
subdominio: kubernetes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://kubernetes.io/docs/concepts/services-networking/network-policies/", "https://kubernetes.io/docs/concepts/security/multi-tenancy/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [Kubernetes NetworkPolicy, Network Policy, Isolamento de rede de Pods]
lote: software-kubernetes-operacao-0005
---

# Isolamento de rede com NetworkPolicy no Kubernetes

## Em uma frase
NetworkPolicy declara quais conexões IP de entrada e saída são permitidas para Pods selecionados, desde que o plugin de rede do cluster implemente a política.

## Por que importa
Em muitas configurações, Pods podem comunicar-se entre si sem restrição por padrão. Uma política de rede ajuda a limitar caminhos entre componentes e reduz conexões acidentais ou indesejadas. Criar o objeto Kubernetes sozinho não garante filtragem: a enforcement depende da solução de rede implantada no cluster.

## Como funciona
A política seleciona Pods por labels e declara regras de entrada (`Ingress`), saída (`Egress`) ou ambas. Antes de qualquer política aplicável em uma direção, o Pod é não isolado naquela direção. Quando passa a ser isolado, conexões permitidas são a união aditiva das regras de todas as políticas aplicáveis. Em uma conexão entre Pods, tanto a regra de saída da origem quanto a regra de entrada do destino precisam permitir o fluxo quando ambos os lados estão isolados. Regras podem selecionar Pods, namespaces, blocos CIDR e portas, dentro das capacidades descritas pela API.

## Exemplo
Comece com uma política default-deny para entrada e saída no namespace e acrescente regras explícitas para DNS, entrada do gateway e comunicação entre serviços necessária. Faça isso em etapas: negar egress sem uma exceção de DNS pode impedir resolução de nomes e interromper aplicações.

## Limites e trade-offs
O plugin de rede precisa suportar NetworkPolicy; caso contrário, o recurso não tem efeito. Políticas são aditivas e não oferecem uma regra explícita de negação que se sobreponha a uma permissão existente. É preciso considerar tráfego para DNS, dependências externas, nós e componentes de infraestrutura. NetworkPolicy não substitui autenticação, criptografia de transporte ou controles de aplicação.

## Como verificar
Confirme qual CNI está em uso e valide que ele implementa as regras configuradas. Teste tráfego permitido e bloqueado a partir dos Pods selecionados, nas direções de entrada e saída, observando os fluxos reais e não apenas o objeto no API server. Revise labels dos seletores, namespace e exceções de DNS durante o rollout.

## Conexões
- [[rbac-kubernetes-serviceaccounts]] — permissões sobre objetos de rede e permissões sobre tráfego são controles distintos.
- [[secrets-kubernetes-protecao-dados]] — isolamento de rede complementa a proteção de credenciais montadas em Pods.
- [[probes-kubernetes-liveness-readiness-startup]] — bloqueios de rede podem afetar readiness e dependências de serviço.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — pré-requisitos, seleção, isolamento e agregação de regras; acesso em 2026-10-01.
- [Kubernetes — Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/) — contexto de isolamento de rede entre Pods; acesso em 2026-10-01.
