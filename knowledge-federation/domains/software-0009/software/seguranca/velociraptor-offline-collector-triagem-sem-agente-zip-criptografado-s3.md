---
id: software.seguranca.tranche03.000295
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://docs.velociraptor.app/docs/overview/", "https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md", "https://github.com/Velocidex/velociraptor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Velociraptor `Offline Collector`: geração de binário autônomo pré-configurado para triagem forense com upload cifrado (`ZIP` / `S3` / `Azure`)

## Em uma frase
Conforme documentado tanto no README oficial (*Running Velociraptor locally*) quanto na seção *Offline collector* de `docs.velociraptor.app/docs/overview/`, quando o agente do Velociraptor ainda não está instalado na máquina alvo (por exemplo, quando uma consultoria DFIR acaba de ser acionada ou em servidores DMZ isolados), o Velociraptor compila um **Offline Collector (`Server.Utils.CreateCollector`)**!

## Por que importa
Em uma resposta a incidente emergencial, instalar dezenas de ferramentas forenses e dependências Python em um servidor comprometido altera evidências e consome tempo precioso.

## Como funciona
O **Offline Collector** é um único executável standalone pré-configurado com os artefatos escolhidos (ex.: `Windows.KapeFiles.Targets`, `Windows.System.Pslist`, dumps de registro e `$MFT`): basta executá-lo no host alvo e ele coleta todas as evidências em um **arquivo `.zip` protegido por senha ou chave pública X.509** e pode fazer upload automático direto para um bucket **AWS S3**, **GCS**, **Azure Blob** ou SFTP!

## Exemplo
```bash
# Importando um pacote ZIP coletado por um Offline Collector para dentro do servidor Velociraptor para análise no Notebook:
velociraptor --config server.config.yaml artifacts collect Server.Utils.ImportCollection \
  --args ZipFilename=/cases/Collection-HOST01-2026.zip
```

## Limites e trade-offs
Como destaca a documentação oficial, você também pode distribuir e executar o *Offline Collector* remotamente usando um EDR já existente na empresa, **Group Policy (GPO)**, **Intune**, **SSM** ou **Ansible**, e reimportar todos os `.zip` no servidor Velociraptor criando *Virtual Clients*!

## Como verificar
Gere um coletor offline pelo menu `Server Artifacts -> Build Collector` da GUI e valide o arquivo `.zip` produzido.

## Conexões
- [[velociraptor-hunting-at-scale-controle-recursos-cpu-iops-rate-limiting]] — Veja também: Velociraptor `Hunts` em Escala e Controle de Recursos no Endpoint: `ops_per_second`, limite de CPU (`max_cpu`) e `timeout`.
- [[velociraptor-monitoramento-tempo-real-client-events-etw-ebpf-sigma]] — Veja também: Velociraptor Detecção em Tempo Real (`CLIENT_EVENT`): monitoramento contínuo via `ETW` (Windows), `eBPF` (Linux) e regras `Sigma`.

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
