---
id: software.devops.tranche08.000718
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md", "https://github.com/firecracker-microvm/firecracker/blob/main/SPECIFICATION.md", "https://github.com/firecracker-microvm/firecracker"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# AWS Firecracker: especificação de performance verificada em CI e sistema de logging e métricas via API

## Em uma frase
O Firecracker mantém compromissos formais de performance e footprint documentados em `SPECIFICATION.md` (verificados continuamente no pipeline de CI) e expõe configuração de logs e métricas operacionais via API (`/logger` e `/metrics`).

## Por que importa
Em infraestruturas de alta densidade, qualquer regressão acidental de código que aumente o consumo de memória base do VMM em alguns megabytes ou adicione dezenas de milissegundos ao tempo de boot da microVM impacta diretamente a economia de toda a frota serverless; além disso, o operador precisa coletar telemetria de emulação, I/O e erros sem instalar agentes pesados dentro da microVM. O README oficial do Firecracker detalha o documento `SPECIFICATION.md` e o sistema de logging/métricas.

## Como funciona
Por meio dos endpoints `/logger` e `/metrics` na API do Firecracker, o plano de controle no host configura arquivos (ou named pipes / FIFOs pré-criados dentro da jaula do `jailer`) onde o VMM grava logs estruturados e despeja periodicamente contadores JSON detalhados sobre chamadas de API, falhas de página, pacotes e bytes de `virtio-net`, operações de `virtio-block`, sinais e eventos de vCPU. Paralelamente, todas as características de desempenho prometidas pelo projeto em `SPECIFICATION.md` (tempo de inicialização até o código de usuário, overhead de memória por microVM e performance de rede/bloco) são impostas automaticamente por testes de integração contínua a cada mudança.

## Exemplo
```bash
# Configurar o subsistema de métricas e logs de uma microVM Firecracker via API apontando para FIFOs/arquivos locais
curl --unix-socket /tmp/firecracker.socket -i -X PUT "http://localhost/metrics" \
  -H "Content-Type: application/json" \
  -d '{"metrics_path": "/tmp/fc-metrics.fifo"}'
```

## Limites e trade-offs
Quando `/logger` ou `/metrics` são configurados apontando para um named pipe (FIFO) no host a fim de fazer streaming em tempo real sem gravar em disco, o processo leitor no host deve consumir continuamente os dados do FIFO; se o leitor travar ou fechar o pipe, o buffer do pipe encherá, podendo descartar métricas ou afetar o registro de logs da microVM.

## Como verificar
Configure `/metrics` apontando para um arquivo local na microVM de teste e inspecione o JSON emitido para verificar os contadores de `block`, `net`, `vcpu` e `api_server`.

## Conexões
- [[firecracker-plataformas-testadas-intel-amd-graviton-kernels]] — Veja também: AWS Firecracker: matriz de plataformas bare-metal testadas (Intel, AMD, ARM Graviton) e requisitos de kernel.
- [[firecracker-integracao-container-runtimes-kata-flintlock]] — Veja também: AWS Firecracker: integração com runtimes de containers e microVMs (Kata Containers e Flintlock).
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[firecracker-api-openapi-configuracao-vcpu-memoria-boot]] — Referência cruzada direta com firecracker-api-openapi-configuracao-vcpu-memoria-boot.
- [[firecracker-demand-fault-paging-oversubscription-cpu-memoria]] — Referência cruzada direta com firecracker-demand-fault-paging-oversubscription-cpu-memoria.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/SPECIFICATION.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
