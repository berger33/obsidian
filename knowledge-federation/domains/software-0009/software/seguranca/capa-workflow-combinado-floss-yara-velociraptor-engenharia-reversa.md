---
id: software.seguranca.tranche13.001230
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/capa/master/README.md", "https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Workflow Integrado de Análise de Malware e DFIR: Combinando **Mandiant `FLOSS` + `capa` + `YARA` + `Velociraptor` / `Plaso`**

## Em uma frase
Como as ferramentas open-source que estudamos se encaixam em um fluxo de trabalho coeso e profissional de **Engenharia Reversa e Resposta a Incidentes (DFIR)** desde o minuto zero em que um arquivo suspeito é encontrado em um host?

## Por que importa
Conectar a extração de strings desofuscadas com a detecção estrutural de capacidades reduz o tempo entre a coleta da amostra e a contenção na frota de horas para poucos minutos.

## Como funciona
O pipeline de referência de laboratórios FLARE / CSIRT segue quatro etapas encadeadas: **(1) Extração de Strings e Desofuscação com `FLOSS` (`floss amostra.exe`)** — extrai em segundos todas as strings estáticas, *stack strings*, *tight strings*, strings decodificadas em memória por emulação e strings específicas de Go/Rust (revelando domínios de C2, chaves de registro, mutexes e caminhos de arquivos que o `strings` comum do Unix jamais veria!); **(2) Mapeamento de Capacidades com `capa` (`capa -vv amostra.exe`)** — identifica todas as técnicas ATT&CK/MBC e aponta os endereços exatos das funções críticas para o Ghidra/IDA; **(3) Criação de Regra `YARA` de Alta Fidelidade** combinando os opcodes das funções apontadas pelo `capa` com as strings exclusivas reveladas pelo `FLOSS`; e **(4) Caça Retroativa (*Threat Hunting*) na Frota com `Velociraptor` / `Plaso`**!

## Exemplo
```bash
# Pipeline de triagem estatica automatizada combinando FLOSS (strings desofuscadas), capa (capacidades) e YARA em uma amostra
floss -j ./amostras/implant.exe > ./triage_floss.json
capa -j ./amostras/implant.exe > ./triage_capa.json
yara -s ./regras/apt_custom.yar ./amostras/implant.exe
```

## Limites e trade-offs
Por que rodar o **`FLOSS` e o `capa` juntos** na triagem inicial multiplica a velocidade da resposta a incidentes? Porque enquanto o **`capa`** responde *"Como o malware funciona e onde estão suas funções críticas?"*, o **`FLOSS`** responde *"Para qual IP/domínio ele conecta, qual chave de registro ele cria e quais comandos ele aceita?"* — entregando os **IOCs de rede e host** prontos para bloqueio no Firewall/EDR em poucos minutos!

## Como verificar
Guarde os arquivos `triage_floss.json` e `triage_capa.json` anexados ao ticket do incidente para consulta de toda a equipe.

## Conexões
- [[capa-uso-biblioteca-python-automacao-pipelines-triagem-malware-soc]] — Veja também: Usando o `capa` como **Biblioteca Python (`capa.main`, `capa.rules`, `capa.engine`)**: Construindo Pipelines Automatizados de Triagem de Malware e Validação de Builds.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
