---
id: software.seguranca.tranche11.001059
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/angr/angr/master/README.md", "https://docs.angr.io/en/latest/quickstart.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria de Firmware IoT com `angr` (**`Firmalice`**): Detecção Automática de **Backdoors e Authentication Bypass** em Binários Embarcados

## Em uma frase
O terceiro paper fundador citado na documentação oficial do `angr` (`quickstart.html`) é **`Firmalice — Automatic Detection of Authentication Bypass Vulnerabilities in Binary Firmware` (NDSS 2015)**.

## Por que importa
Qual é a ideia central por trás do modelo *Firmalice* no `angr`? Em roteadores, câmeras IP, CLPs industriais e dispositivos IoT, fabricantes frequentemente deixam contas de manutenção ocultas, senhas mestre *hardcoded* ou caminhos lógicos onde uma requisição HTTP específica alcança uma **Operação Privilegiada** (ex.: executar comandos via `system()`, abrir um shell telnet ou alterar configurações administrativas) sem passar por uma validação real de credenciais do banco de usuários!

## Como funciona
Com o `angr`, você modela uma **Operação Privilegiada como o endereço alvo (`find=addr_operacao_privilegiada`)**, inicia um `call_state` ou `blank_state` na função de tratamento de requisições do servidor web embarcado (`httpd` / `goahead` / `boa`) e pede ao `SimulationManager` para encontrar uma entrada simbólica que alcance a operação privilegiada: se o solver Z3 produzir uma string constante determinística (ex.: `User-Agent: xmlset_roodkcableoj28840ybtide`), você acabou de descobrir um backdoor *hardcoded* no firmware!

## Exemplo
```python
import angr
import claripy

# Exemplo de setup para analisar uma funcao especifica de autenticacao de firmware IoT com call_state e argumentos simbolicos
proj = angr.Project("/bin/true", auto_load_libs=False)
senha_ptr = 0x600000
senha_sym = claripy.BVS("password_input", 8 * 16)

# Iniciar estado diretamente no endereco de uma funcao alvo passando o ponteiro para o buffer simbolico no 1o argumento
state = proj.factory.call_state(proj.entry, senha_ptr)
state.memory.store(senha_ptr, senha_sym)
print("Estado configurado no endereco:", hex(state.addr))
```

## Limites e trade-offs
Por que usar **`proj.factory.call_state(addr_funcao, arg1, arg2)`** é a técnica preferida ao auditar binários gigantes de firmware IoT (como um binário `httpd` de 4 MB em arquitetura MIPS ou ARM)? Porque em vez de tentar simular toda a inicialização de hardware, NVRAM e sockets desde o `main()`, você começa a execução simbólica **diretamente no endereço da função suspeita** (`addr_funcao`), passando ponteiros para buffers simbólicos nos argumentos!

## Como verificar
Combine a triagem estática no **Ghidra** (para localizar os endereços das funções de parse de autenticação) com o `call_state` do `angr` (para resolver as restrições exatas de entrada).

## Conexões
- [[angr-execucao-concolica-hibrida-fuzzing-driller-afl-qiling-unicorn]] — Veja também: Execução Concólica Híbrida e Fuzzing Assistido por Solver (**`Driller`**) & Engine Nativa **Unicorn (`angr.options.UNICORN`)**.
- [[angr-descoberta-vulnerabilidades-memoria-unconstrained-bof-aeg-rop]] — Veja também: Caça a Corrupção de Memória e **Exploit Generation (`save_unconstrained=True` & `angrop`)**: Encontrando e Explorando **Stack Buffer Overflows** com `angr`.
- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — Referência cruzada direta com angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy.
- [[angr-carregador-binarios-cle-shared-libraries-firmware-blobs-base-addr]] — Referência cruzada direta com angr-carregador-binarios-cle-shared-libraries-firmware-blobs-base-addr.

## Fontes
- [angr Official GitHub — Platform-Agnostic Binary Analysis & Symbolic Execution Framework](https://raw.githubusercontent.com/angr/angr/master/README.md) — repositório oficial do `angr` cobrindo carregamento de binários, lifting para IR, execução simbólica, hooks e decompilação; consultado em 2026-10-03.
- [angr Official Documentation — Quickstart, Architecture & Foundational Research (`SoK`, `Driller`, `Firmalice`)](https://docs.angr.io/en/latest/quickstart.html) — documentação oficial do `angr` detalhando os subsistemas `CLE`, `PyVEX`, `Claripy`, `SimState`, `SimulationManager` e análises estáticas/concólicas; consultado em 2026-10-03.
