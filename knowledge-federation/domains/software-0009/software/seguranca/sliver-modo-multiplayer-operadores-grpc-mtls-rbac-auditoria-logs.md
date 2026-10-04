---
id: software.seguranca.tranche16.001544
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/BishopFox/sliver/master/README.md", "https://sliver.sh/docs?name=Getting+Started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Operação em Equipe (**Multiplayer Mode** sobre gRPC mTLS), Gerenciamento de Operadores (**`new-operator`**) e **Audit Log JSON** Completo para Purple Team no Sliver

## Em uma frase
Como múltiplos especialistas de Red Team trabalham simultaneamente na mesma operação do **Sliver** a partir de suas próprias estações de trabalho, e como o líder do exercício (ou o time de Purple Team) audita **cada comando digitado, cada arquivo baixado e cada resposta recebida com timestamp exato** ao final do teste?

## Por que importa
Primeiro: o Sliver utiliza o **Multiplayer Mode** nativo sobre **gRPC com Mutual TLS (`mTLS`)**! No servidor Linux, você cria um perfil de acesso individual para cada operador com **`new-operator --name alice --lhost 10.0.0.5`** (gerando um arquivo `.cfg` contendo o certificado X.509 e a chave privada exclusiva de `alice`) e ativa o listener `multiplayer`.

## Como funciona
Segundo: o Sliver grava automaticamente um **Audit Log estruturado em JSON (`~/.sliver/logs/audit.json`)** que registra **100% dos comandos executados por todos os operadores e todos os eventos de implantes** — permitindo correlacionar segundo a segundo o que o Red Team fez com o que o SIEM/EDR do Blue Team detectou!

## Exemplo
```bash
# Gerar no servidor Sliver um arquivo de configuracao mTLS para um operador remoto e importar o perfil no sliver-client
sliver-server operator --name operador_alice --lhost 192.0.2.100 --save ./alice.cfg
sliver-client import ./alice.cfg
```

## Limites e trade-offs
Por que o arquivo **`~/.sliver/logs/audit.json`** do Sliver vale ouro em exercícios de **Purple Team** e em relatórios de Pentest? Porque ao terminar a operação, você pode filtrar `audit.json` com `jq` para gerar uma **Linha do Tempo Automática (*Attack Timeline*)** com o horário UTC exato de cada técnica MITRE ATT&CK executada, facilitando medir o **MTTD (*Mean Time To Detect*)** do SOC!

## Como verificar
Quando um operador sai da operação ou termina seu turno, você pode revogar instantaneamente o certificado mTLS dele no servidor sem afetar os demais operadores nem os implantes ativos!

## Conexões
- [[sliver-protocolos-transporte-mtls-wireguard-https-dns-traffic-encoders]] — Veja também: Engenharia dos 4 Canais de Transporte C2 do Sliver (**`mtls`**, **`wg` WireGuard**, **`https` C2 Profiles** e **`dns` Canário**) e **Traffic Encoders (Wasm)**.
- [[sliver-execucao-em-memoria-bof-coff-execute-assembly-sideload-spawndll]] — Veja também: Pós-Exploração *In-Memory* no Sliver: **BOF / COFF Loader (`Armory`)**, **`execute-assembly` (.NET CLR)**, **`sideload`** e **`spawndll`** sem Tocar o Disco.
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Referência cruzada direta com sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
