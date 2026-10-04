---
id: software.devops.tranche06.000593
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/nomad/main/README.md", "https://developer.hashicorp.com/nomad/docs", "https://github.com/hashicorp/nomad"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte nativo a cargas de IA/ML com Device Plugins para GPUs, FPGAs e TPUs no Nomad

## Em uma frase
A seção *Device Plugins & GPU Support* do README oficial destaca que o Nomad oferece **suporte embutido para cargas de trabalho de GPU, como Machine Learning (ML) e Inteligência Artificial (AI)**: através de sua arquitetura de **Device Plugins**, o agente cliente do Nomad **detecta automaticamente e utiliza recursos de dispositivos de hardware especializados, como GPUs (NVIDIA, AMD), FPGAs e TPUs**, expondo seus atributos (modelo, memória de vídeo, topologia) para o agendador.

## Por que importa
Em clusters de treinamento e inferência de IA/ML ou processamento de vídeo em tempo real, o agendador precisa saber exatamente quantas placas de GPU livres existem em cada servidor físico, qual o modelo da GPU (ex.: A100 vs H100 vs T4) e alocar o dispositivo com isolamento correto para a tarefa solicitante sem conflito entre jobs concorrentes.

## Como funciona
Habilite o bloco de `plugin` de dispositivo correspondente na configuração dos nós clientes do Nomad que possuem placas aceleradoras e declare o bloco `device "nvidia/gpu" { count = ... }` dentro da especificação `resources` da tarefa no seu job HCL.

## Exemplo
Uma equipe de IA submete um job de treinamento distribuído ao Nomad exigindo `device "nvidia/gpu" { count = 2 }` com restrição de memória mínima de VRAM; o agendador do Nomad localiza automaticamente os nós com GPUs compatíveis livres e injeta os dispositivos no contêiner da tarefa.

## Limites e trade-offs
Combine o uso de Device Plugins de GPU com afinidades ou restrições de classe de nó (`node_class`) para evitar que jobs comuns de CPU que não precisam de aceleradores ocupem toda a memória RAM de servidores caros equipados com GPUs.

## Como verificar
Execute `nomad node status -verbose <node-id>` em um host com acelerador e confirme a listagem da placa e de suas estatísticas na seção `Host Devices`.

## Conexões
- [[nomad-single-binary-self-contained-architecture]] — Veja também: Arquitetura de binário único autocontido do Nomad sem serviços externos de armazenamento ou coordenação.
- [[nomad-multi-region-and-multi-cloud-federation-out-of-the-box]] — Veja também: Federação nativa Multi-Região e Multi-Cloud em escala global no Nomad.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
