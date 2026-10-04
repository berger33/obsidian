---
id: software.seguranca.tranche16.001550
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

# Engenharia de Detecção (**Blue Team / SOC / NSM**) Contra Implantes **Sliver C2**: Assinaturas **JARM/JA4 TLS**, Caça a Beacons no **RITA/Zeek** e **YARA em Memória**

## Em uma frase
Acabamos de estudar como o **Sliver C2** opera do ponto de vista ofensivo (Red Team). Agora, virando a mesa para a **Engenharia de Detecção (Blue Team / DFIR / Threat Hunting)**: quais são os 4 sinais técnicos mais eficazes para detectar implantes e servidores do **Sliver C2** na sua rede e nos seus endpoints?

## Por que importa
Veja as 4 camadas de detecção comprovadas: **(Camada 1 — Fingerprinting Ativo/Passivo TLS `JARM` e `JA4/JA4S` no Zeek/Suricata)**: a pilha TLS nativa do Go (`crypto/tls`) usada pelo listener `mtls`/`https` do `sliver-server` e pelos implantes Go produz assinaturas **`JARM` e `JA4`** características que diferem do navegador Chrome/Edge padrão do Windows!

## Como funciona
**(Camada 2 — Análise Matemática de Beaconing no RITA + Zeek)**: mesmo com `--jitter 30`, após algumas horas de check-ins periódicos para o mesmo IP/SNI externo sem ser um site popular (`Prevalence = 1 host`), o **RITA** pontua o beacon do Sliver no topo do ranking; **(Camada 3 — Monitoramento de Anomalias de Processo/Rede no Endpoint)**: binários não assinados fazendo conexões TLS periódicas ou carregando `clr.dll` (`execute-assembly`); e **(Camada 4 — Varredura de Memória com YARA / Velociraptor / Mandiant `capa`)**!

## Exemplo
```bash
# Auditar conexoes suspeitas no Linux/Windows procurando binarios Go (Sliver) em memoria com YARA ou inspecionando beacons no RITA
rita view --stdout ./resultados_zeek_hoje | head -n 15
yara -s ./regras_sliver_golang.yar /proc/$(pidof processo_suspeito)/mem
```

## Limites e trade-offs
Por que escanear a **Memória do Processo (`/proc/<pid>/mem` no Linux ou via Velociraptor `Windows.Detection.Yara.Process` no Windows)** com **YARA** pega implantes Sliver mesmo quando eles foram carregados via Stager *in-memory* ou empacotados? Porque uma vez descompactado e em execução na memória RAM, as estruturas internas de tipos Protobuf (`sliverpb`) e metadados de runtime do Go ficam visíveis na memória do processo!

## Como verificar
Com isso concluímos o módulo do **Sliver C2** cobrindo tanto a operação de Red Team quanto a engenharia de detecção de Blue Team!

## Conexões
- [[sliver-extensao-cursed-chrome-electron-debug-port-post-exploitation]] — Veja também: Pós-Exploração de Navegadores e Apps **Electron (`Slack`, `VS Code`, `Teams`, `Discord`)** com o Subsistema **`cursed`** do Sliver.
- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Referência cruzada direta com sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns.

## Fontes
- [Sliver Adversary Emulation Framework Official Repository (`BishopFox/sliver`)](https://raw.githubusercontent.com/BishopFox/sliver/master/README.md) — repositório oficial do framework C2 Sliver em Go cobrindo implantes multi-plataforma, chaves assimétricas únicas por binário e execução BOF/COFF; consultado em 2026-10-03.
- [Sliver Official Documentation — Getting Started (`sliver.sh/docs?name=Getting+Started`)](https://sliver.sh/docs?name=Getting+Started) — documentação oficial do Sliver detalhando arquitetura Server/Multiplayer, diferença entre `Beacon Mode` e `Session Mode`, geração de implantes, `interactive` e Stagers; consultado em 2026-10-03.
